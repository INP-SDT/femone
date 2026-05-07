# -*- coding: utf-8 -*-
"""Convection-diffusion test.
"""
import numpy as np
from scipy import sparse as sp
import femone as fem

DIFF = globals().get('DIFF') or 1.0
VELY = globals().get('VELY') or 0.0

TAU = 2e-5
N_T = 500

# MESH

mesh = fem.mesh.getmesh(
    np.linspace(0., 1., 501)
)

# UNIT

unit = fem.fem.getunit(mesh)

# OPERATORS

M = unit.makemat(unit.massmat)
D = unit.makemat(unit.diff_2x)
V = unit.makemat(unit.diff_1x)

A = M - TAU * (VELY * V - DIFF * D)

A[+0, +0] = 1.0
A[+0, +1] = 0.0

A[-1, -1] = 1.0
A[-1, -2] = 0.0

# SOLUTION

sol = np.ones_like(
    unit.mesh.points
)

for _ in range(N_T):

    rhs = M @ sol

    rhs[+0] = 0.0
    rhs[+1] = 0.0

    sol = sp.linalg.spsolve(A, rhs)

xax = unit.xax
