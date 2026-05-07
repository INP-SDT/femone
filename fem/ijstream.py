# -*- coding: utf-8 -*-
"""IJ-stream.
"""
import numpy as np


def get_ijstream(mesh):
    """Creates an IJ-stream from a mesh.
    """
    return StreamMaker.from_mesh(mesh).get_ij_stream()


class StreamMaker:
    """Maker of an ij-stream.
    """

    def __init__(self, mesh):
        self.mesh = mesh

    @classmethod
    def from_mesh(cls, mesh):
        return cls(mesh)

    def get_ij_stream(self):

        data = [
            self.get_i_stream(),
            self.get_j_stream(),
            self.get_e_stream()
        ]

        return IJStream.from_data(np.vstack(data))

    def get_i_stream(self):

        data = np.repeat(
            self.mesh.elements, 2, axis=1
        )

        return data.flatten()

    def get_j_stream(self):

        data = np.tile(
            self.mesh.elements, (1, 2)
        )

        return data.flatten()

    def get_e_stream(self):

        nums = np.arange(
            self.mesh.elements.shape[0]
        )

        data = np.tile(nums, (4, 1))
        return data.T.flatten()


class IJStream:
    """Stream of ij-coordinates.
    """

    def __init__(self, data):
        self.data = data

    @classmethod
    def from_data(cls, data):
        return cls(data)

    @property
    def rownums(self):
        return self.data[0, :]

    @property
    def colnums(self):
        return self.data[1, :]

    @property
    def elmnums(self):
        return self.data[2, :]
