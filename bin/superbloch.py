import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from numpy import pi
from lz.lz import lz_grid_time_evolution

params = dict(
    T_grid = 5,
    T_bloch = 4*pi/5,
    s = 0.6,
    sigma = 0.01,
    t_end = 500,
    n = 160,
    n_times = 201,
)

lz_grid_time_evolution(**params)
