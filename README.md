# Time-energy Bloch oscillations

Simulations for the paper "Bloch-like energy oscillations" (Phys. Rev. A 98, 053820) by Axel Gagge and Jonas Larson.

You can find the paper itself here:

- https://arxiv.org/abs/1808.08061
- https://journals.aps.org/pra/abstract/10.1103/PhysRevA.98.053820

## Requirements and running

Make sure you have Python version 3.6 or higher installed. The following Python packages are required:

- numpy
- matplotlib
- [qutip)](http://qutip.org/)

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
