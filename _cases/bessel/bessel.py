# -*- coding: utf-8 -*-
"""Reproducing Bessel function.
"""
import numpy as np
from matplotlib import pyplot as plt
from scipy import sparse as sp
from scipy.special import j0
import femone as fem

X_0 = 10.
N_X = 101

# MESH

mesh = fem.mesh.getmesh(
    np.linspace(0., X_0, N_X)
)

# UNIT

unit = fem.fem.getunit(mesh)

# OPERATOR

geom = unit.cax[unit.ij_e]

A = unit.makemat(
    - unit.diff_2x + unit.massmat + unit.grad_1x / geom
)

b = np.zeros_like(unit.xax)

# BC

A[-1, -1] = 1.0
A[-1, -2] = 0.0

b[-1] = j0(X_0)

# SOLUTION

sol = sp.linalg.spsolve(A, b)

plt.plot(unit.xax, sol, '.b')
plt.plot(unit.xax, j0(unit.xax), '-r')
