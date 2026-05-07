# -*- coding: utf-8 -*-
"""FEM (P1) solver.
"""
import numpy as np
from scipy import sparse as sp
from femone.fem import ijstream
from femone.fem import vstreams
from femone.fem import matmaker


def getunit(mesh):
    """Creates a FEM computing unit.

    Parameters
    ----------
    mesh : Mesh
        Mesh object.

    Returns
    -------
    FEMUnit
        Resulting FEM unit.

    """
    return FEMUnit.from_mesh(mesh)


class FEMData:
    """Root of the FEM unit.
    """

    def __init__(self, mesh, meta):
        self.mesh = mesh
        self.meta = meta
        self.cache = {}

    @classmethod
    def from_mesh(cls, mesh):
        return UnitMaker(mesh).getunit()

    @property
    def massmat(self):
        return self.meta['vstreams']['massmat'].data

    @property
    def massdig(self):
        return self.meta['vstreams']['massdig'].data

    @property
    def diff_1x(self):
        return self.meta['vstreams']['diff_1x'].data

    @property
    def grad_1x(self):
        return self.meta['vstreams']['grad_1x'].data

    @property
    def diff_2x(self):
        return self.meta['vstreams']['diff_2x'].data

    @property
    def ij_r(self):
        return self.meta['ijstream'].rownums

    @property
    def ij_c(self):
        return self.meta['ijstream'].colnums

    @property
    def ij_e(self):
        return self.meta['ijstream'].elmnums

    @property
    def xax(self):
        return self.mesh.points

    @property
    def cax(self):
        return self.mesh.centrs


class FEMUnit(FEMData):
    """FEM computing unit.

    Properties
    ----------

    Basic FEM operators as data-streams:

    Name        | Description
    ------------|------------------------------------
    `massmat`   | Mass-matrix
    `massdig`   | Mass-matrix (lumped)
    `diff_1x`   | 1st derivative (weak)
    `grad_1x`   | 1st derivative (strong)
    `diff_2x`   | 2nd derivative (weak)

    Indexers of a data-stream:

    Name        | Description
    ------------|-------------------------------------
    `ij_r`      | Row numbers in a data stream
    `ij_c`      | Column numbers in a data stream
    `ij_e`      | Element numbers in a data stream

    General properties:

    Name        | Description
    ------------|-------------------------------------
    `xax`       | Shortcut for mesh points.
    `cax`       | Shortcut for mesh midpoints.
    `mass`      | Mass matrix.

    """

    @property
    def mass(self):

        if 'massmat' in self.cache:
            return self.cache['massmat']

        self.cache['massmat'] = self.makemat(self.massmat)
        return self.mass

    @property
    def mass_inv(self):

        if 'massmat-inv' in self.cache:
            return self.cache['massmat-inv']

        self.cache['massmat-inv'] = sp.linalg.splu(self.mass)
        return self.mass_inv

    def makemat(self, operator):
        """Creates a FEM matrix.

        Parameters
        ----------
        operator : flat-float-array
            FEM operator as a linear combination of basic FEM operators.

        Returns
        -------
        csc_array
            Sparse matrix in CSC form.

        """
        return matmaker.makemat(self, operator)

    def vec_from_func(self, func):
        """Creates a vector defined on mesh points.

        Parameters
        ----------
        func : Callable
            Defines vector data.

        Returns
        -------
        flat-float-array
            Resulting vector.

        """
        return func(self.mesh.points)

    def vec_with_body(self, body):
        """Creates a vector defined on mesh points.

        Parameters
        ----------
        body : float | flat-float-array
            Defines the vector body.

        Returns
        -------
        flat-float-array
            Resulting vector.

        """
        data = np.zeros_like(self.mesh.points)
        data[:] = body
        return data

    def project_p0_p1(self, data):
        """Projects P0 data to P1 space.

        Parameters
        ----------
        data : flat-float-array
            Input P0 data.

        Returns
        -------
        flat-float-array
            Resulting P1 data.

        """

        q_1 = np.pad(
            data * self.mesh.steps * 0.5, (1, 0)
        )

        q_2 = np.pad(
            data * self.mesh.steps * 0.5, (0, 1)
        )

        return self.mass_inv.solve(q_1 + q_2)

    def project_p1_p0(self, data):
        """Projects P1 data to P0 space.

        Parameters
        ----------
        data : flat-float-array
            Input P1 data.

        Returns
        -------
        flat-float-array
            Resulting P0 data.

        """
        return 0.5 * (
            data[:-1] + data[1::]
        )


class UnitMaker:
    """Maker of the FEM unit.
    """

    def __init__(self, mesh):
        self.mesh = mesh

    def getunit(self):

        meta = self.make_meta()
        unit = self.from_meta(meta)

        return unit

    def from_meta(self, meta):
        return FEMUnit(self.mesh, meta)

    def make_meta(self):
        return {
            'ijstream': self.make_ijstream(),
            'vstreams': self.make_vstreams()
        }

    def make_ijstream(self):
        return ijstream.get_ijstream(self.mesh)

    def make_vstreams(self):
        return vstreams.get_vstreams(self.mesh)
