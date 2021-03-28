# Time-energy Bloch oscillations

Simulations for the paper "Bloch-like energy oscillations" (Phys. Rev. A 98, 053820) by Axel Gagge and Jonas Larson.

You can find the paper itself here:

- [https://arxiv.org/abs/1808.08061]
- [https://journals.aps.org/pra/abstract/10.1103/PhysRevA.98.053820]

![bloch](/fig/bloch.png "Bloch oscillations")

![superbloch](/fig/superbloch.png "Super-Bloch oscillations")

These simulations time-evolve a Gaussian quantum state of width σ in time steps dt, using a
time-dependent Hamiltonian

$$
H_{LZg}(t) = ω (Sz ⊗ 1) + λ t (1 ⊗ σz) + J (A ⊗ σx)
$$

where $Sz = diag(..., -1, 0, 1, ...)$ and A is a n x n matrix with 1 in all
slots. This is a generalization of a Landau-Zener crossing, and a periodic Hamiltonian for infinite matrix size.

The crossings occur at times which are multiples of ω/λ. The Bloch oscillations occur with a period T_bloch = 4π/ω.

For J = 0: the energies cross without gap
For J = 1/π: the adiabatic energies are time-independent, flat

There is a duality: for g = s/π, the width of crossings are the same for s and
1/s.

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
