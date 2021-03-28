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
