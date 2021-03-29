# Time-energy Bloch oscillations

Simulations for the paper "Bloch-like energy oscillations" (Phys. Rev. A 98, 053820) by Axel Gagge and Jonas Larson.

You can find the paper itself here:

- https://arxiv.org/abs/1808.08061
- https://journals.aps.org/pra/abstract/10.1103/PhysRevA.98.053820

![bloch](/fig/bloch.png "Bloch oscillations")

![superbloch](/fig/superbloch.png "Super-Bloch oscillations")

The (time-dependent) Landau-Zener grid Hamiltonian is defined as

![hamiltonian](/fig/h.png "Hamiltonian")

where $S_z = diag(..., -1, 0, 1, ...)$ and A is a n x n matrix with 1 in all
slots. This is a generalization of a Landau-Zener crossing, and is periodic in time for infinite matrix size. The crossings occur at times which are multiples of ω/λ. Further features of the Hamiltonian:

- for J = 0: the energies cross without gap
- for J = 1/π: the adiabatic energies are time-independent, flat
- for J = s/π, the width of crossings appear to be the same for s and 1/s

In the paper, we show that the dynamics in such a system can be described as a 1D tight-binding model, where the  adiabatic eigenstates (eigenstates of the Hamiltonian at each time t) form the "sites" and the first diabatic corrections act like hopping terms. The energy difference between the adiabatic energies, averaged over one period, acts like a constant force on the adiabatic eigenstates. It is well known that such a force leads to Bloch oscillations, which here occur with a period T_bloch = 4π/ω. Beyond the average over a period ω/λ, there are also *super-Bloch oscillations* due to beating effects, since the energy difference between eigenstates varies within each period.

In the simulations, we prepare an initial quantum state which is a Gaussian superposition of adiabatic eigenstates, of width σ, and time-evolve it. Depending on the width, this leads to breathing-motion or the typical sinusoidal oscillations.

## Requirements and running

Make sure you have Python version 3.6 or higher installed. The following Python packages are required:

- numpy
- matplotlib
- [qutip](http://qutip.org/)

To generate plots files, please run from a terminal with the prompt at the root directory of the project (where this `README.md` file is found)


```bash
> python3 bin/bloch.py
> python3 bin/superbloch.py
```

If you have SSH access to another machine, it is possible to run the computations remotely

```bash
> scp -r $(pwd) <username>@<servername>:~/
> ssh <username>@<servername> "cd ~/${PWD##*/}; nohup python3 bin/bloch.py > /dev/null 2>&1 &"
```

and download the results when they are done

```bash
> scp -r <username>@<servername>:~/${PWD##*/}/fig .
```

## License

The code is licensed under a [GNU GPL v3 license](https://www.gnu.org/licenses/gpl-3.0.html).
