import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lz.lz import lz_grid_time_evolution

params = dict(
    T_grid = 1,
    T_bloch = 20,
    s = 0.75,
    sigma = 0.01,
    n = 80,
    t_end = 2 * 20,
    n_times = 201,
)

lz_grid_time_evolution(**params)
