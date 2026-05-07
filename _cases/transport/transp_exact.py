# -*- coding: utf-8 -*-
"""Convection-diffusion test.
"""
import numpy as np
import scipy as sp


def getsol(size, aval, bval, time):
    return ConvDiff.from_params(size, aval, bval).getsol(time)


class ConvDiff:
    """Convection-diffusion test.
    """

    def __init__(self, size, aval, bval):
        self.size = size
        self.aval = aval
        self.bval = bval

    @classmethod
    def from_params(cls, size, aval, bval):
        return cls(size, aval, bval)

    def getsol(self, time):
        """Returns the solution at the specified time.
        """

        mat = self.get_tmatrix(time)
        sol = self.get_uniform()

        return {
            'x': self.xaxs,
            'u': mat @ sol
        }

    def get_uniform(self):
        return np.ones(self.size - 1)

    def get_tmatrix(self, time):
        """Time-step matrix.
        """

        symm = self.get_symmer()
        eigv = self.get_eigval()

        core = np.diag(
            np.exp(time*eigv['L'])
        )

        west = symm['Q1'] @ eigv['V']
        east = eigv['V'].T @ symm['Q2']

        return west @ core @ east

    def get_eigval(self):
        """Eigenvalue transform.
        """

        aval = self.acoef
        bval = self.bcoef

        d_1 = np.full(
            self.size - 1, - 2 * bval
        )

        d_2 = np.full(
            self.size - 2, np.sqrt(bval ** 2 - aval ** 2)
        )

        out = sp.linalg.eigh_tridiagonal(d_1, d_2)

        return {
            'L': out[0],
            'V': out[1]
        }

    def get_symmer(self):
        """Symmetrizing transform.
        """

        aval = self.acoef
        bval = self.bcoef

        cval = (bval + aval) / (bval - aval)

        diag = np.multiply.accumulate(
            np.full(self.size - 2, cval)
        )

        diag = np.hstack(
            [1., np.sqrt(diag)]
        )

        return {
            'Q1': np.diag(diag),
            'Q2': np.diag(1.0 / diag)
        }

    @property
    def step(self):
        return 1.0 / self.size

    @property
    def xaxs(self):
        return np.linspace(0, 1, self.size + 1)[1:-1]

    @property
    def bcoef(self):
        return (self.bval / self.step) / self.step

    @property
    def acoef(self):
        return (self.aval / self.step) / 2.0

