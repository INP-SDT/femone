# -*- coding: utf-8 -*-
"""Sinwave test.
"""
import numpy as np
from matplotlib import pyplot as plt
import scipy.sparse as sp
import femone as fem

# DATA


def cof(_):
    """Coefficient.
    """
    return 1 + _ * _


def sol(_):
    """Solution.
    """
    return np.sin(2.0 * np.pi * _)


def rho(_):
    """RHS.
    """

    rho_1 = (4.0*np.pi) * _ * np.cos(2*np.pi*_)
    rho_2 = (4.0*np.pi*np.pi) * (_ * _ + 1.0) * np.sin(2*np.pi*_)

    return rho_1 - rho_2

# MESH


mesh = fem.mesh.getmesh(
    np.linspace(0., 1., 201)
)

# UNIT

unit = fem.fem.getunit(mesh)

# OPERATORS

M = unit.makemat(unit.massmat)

A = unit.makemat(
    - cof(unit.cax)[unit.ij_e] * unit.diff_2x
)

b = M @ rho(unit.xax)

# BCs

A[+0, +0] = 1.0
A[+0, +1] = 0.0

A[-1, -1] = 1.0
A[-1, -2] = 0.0

b[+0] = sol(0.0)
b[-1] = sol(1.0)

u = sp.linalg.spsolve(A, b)

# POSTPROCESSOR

err = np.amax(
    np.abs(u - sol(unit.xax))
)

print(err)

plt.plot(unit.xax, u, '-b')

plt.plot(
    unit.xax[::5], sol(unit.xax)[::5], '.r'
)
