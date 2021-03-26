"""Time-evolve a Gaussian state of width σ in time steps dt, using a
time-dependent Hamiltonian

``H_{LZg}(t) = ω (Sz ⊗ 1) + λ t (1 ⊗ σz) + J (A ⊗ σx)``

where ``Sz = diag(..., -1, 0, 1, ...)`` and A is a n x n matrix with 1 in all
slots. This is a generalization of a Landau-Zener crossing.

The crossings occur at times which are multiples of ω/λ.

The Bloch oscillations occur with a period T_bloch = 4π/ω.

Why is the adiabatic energies "unstable" for large t?? Is it because n is
finite?


For J = 0: the energies cross without gap
For J = 1/π: the adiabatic energies are time-independent, flat

There is a duality: for g = s/π, the width of crossings are the same for s and
1/s.


The super-Bloch oscillations occur with a period (?)

T_{sB} ~ 1/abs(1/T_grid - 1/T_B)

T_{sB} ~ 1/abs(1 - 1/T_B) = T_B/abs(T_B-1) = 4 π / (4 π - 1) ~ 1.08

That is not good! We should maybe keep another parameter in the Hamiltonian?

"""


import numpy as np
from qutip import *


def all_ones(n):
    N = 2*n + 1
    offsets = range(-N, N+1)
    diagonals = [np.ones(N-abs(offset)) for offset in offsets]
    return qdiags(diagonals, offsets, dims=None, shape=(N, N))


def adiabatic_eigenstates(H):
    _, states = H.eigenstates()
    return states


def prepare_gaussian_initial_state(H, x0=0.5, sigma=0.01):
    states = adiabatic_eigenstates(H)
    N = states[0].shape[0]//2
    x = np.arange(-(N-1/2), (N+1/2))
    profile = np.exp(-(x/(N*sigma))**2)
    profile /= np.linalg.norm(profile)
    psi = sum([profile[i] * states[i] for i in range(len(states))])
    return psi.unit()


def adiabatic_project(states, psi):
    return np.array([np.abs(np.array(psi.dag() * state)[0, 0]) for state in states])

def hamiltonian(omega, lamda, J, n):
    N = 2*n + 1
    Sz = num(N, offset=-n)
    A = all_ones(n)
    H0 = omega * tensor(Sz, identity(2)) + J * tensor(A, sigmax())
    def H1_args(t, args):
        return lamda * t # np.mod(t, (omega/lamda))
    H1 = [tensor(identity(N), sigmaz()), H1_args]
    H = [H0, H1]
    return H
