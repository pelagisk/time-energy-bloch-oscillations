import numpy as np
import matplotlib.pyplot as plt
from qutip import *
import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lz.system import *


def lz_grid_time_evolution(T_grid=1, T_bloch=10, s=0, sigma=0.01, t_end=1, n=80,
                           n_times=201):
    """
    T_grid = ω / λ
    T_bloch = 4 π / ω
    """

    lamda = 4 * np.pi / (T_grid * T_bloch)
    omega = lamda * T_grid
    J = s / np.pi
    N = 2*n + 1

    id = f"Tgrid={T_grid:.4f}_Tbloch={T_bloch:.4f}_s={s:.4f}_n={n}"

    t_list = np.linspace(0, t_end, n_times)

    # compute Hamiltonian
    H = hamiltonian(omega, lamda, J, n)
    Hfun = QobjEvo(H)

    # TODO is this meaningful to plot?
    # e_values = np.zeros((len(t_list), 2*N))
    # for (j, t) in enumerate(t_list):
    #     e_values[j, :] = Hfun(t).eigenenergies()
    #
    # for j in range(2*n + 1):
    #     plt.plot(t_list, e_values[:, j], 'k-')
    # plt.xlim(min(t_list), max(t_list))
    # plt.xlabel("$t$")
    # plt.ylabel("Energy")
    # plt.title(f"Adiabatic energies for $J = %s/\pi$" % s)
    # plt.savefig(f"fig/adiabatic_energies_{id}.pdf")
    # plt.clf()

    # prepare initial state and verify it
    psi0 = prepare_gaussian_initial_state(Hfun(0.0), sigma)

    # run time evolution and save adiabatic projection at specified times
    data = np.zeros((len(t_list), 2*N))
    global i
    i = 0

    def e_ops(t, psi):
        """Callback measurement function. Here, we diagonalize H(t) and find the
        projections onto each adiabatic eigenstate
        """
        print(t)
        global i
        states = adiabatic_eigenstates(Hfun(t))
        data[i, :] = adiabatic_project(states, psi)
        i += 1

    options = Options(nsteps=1000000)
    sesolve(H, psi0, t_list, e_ops=e_ops, options=options)

    extent = (0, t_list[-1], -N//2, N//2)
    plt.imshow(np.abs(data).T, origin='lower', aspect='auto', extent=extent)
    plt.xlabel("$t$")
    plt.ylabel("n")
    plt.colorbar()
    plt.title(r"$|\langle \psi(t) | \psi_n^{(\rm ad)}(t) \rangle |$")
    plt.savefig(f"fig/time_evolution_{id}.pdf")
