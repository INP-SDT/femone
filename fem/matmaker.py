# -*- coding: utf-8 -*-
"""Maker of FEM matrices
"""
from scipy import sparse as sp


def makemat(unit, opr):
    """Creates a FEM matrix.
    """
    return MatrixMaker.from_unit(unit).make_matrix(opr)


class UnitAgent:
    """Operator on a FEM unit.
    """

    def __init__(self, unit):
        self.unit = unit

    @classmethod
    def from_unit(cls, unit):
        return cls(unit)

    @property
    def ij_tuple(self):
        return (
            self.unit.ij_r, self.unit.ij_c
        )


FEMMatrixError = type(
    'FEMMatrixError', (Exception,), {}
)


class MatrixMaker(UnitAgent):
    """Maker of a FEM matrix.
    """

    def make_matrix(self, opr):

        coo_array = self.make_coo_array(opr)
        csc_array = self.from_coo_array(coo_array)

        if csc_array.has_canonical_format is True:
            return csc_array

        raise FEMMatrixError(
            'FEM matrix does not have the canonical form'
        )

    def from_coo_array(self, arr):
        return arr.tocsc()

    def make_coo_array(self, opr):
        return sp.coo_array((opr, self.ij_tuple))
