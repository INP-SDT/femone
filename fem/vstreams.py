# -*- coding: utf-8 -*-
"""V-streams.
"""
import numpy as np


def get_vstreams(mesh):
    """Makes v-streams from a mesh.
    """
    return StreamsMaker.from_mesh(mesh).get_streams()


class StreamsMaker:
    """Maker of v-streams.
    """

    def __init__(self, mesh):
        self.mesh = mesh

    @classmethod
    def from_mesh(cls, mesh):
        return cls(mesh)

    @property
    def size(self):
        return self.mesh.elements.shape[0]

    def get_streams(self):
        return {
            'massmat': self.get_massmat(),
            'massdig': self.get_massdig(),
            'diff_1x': self.get_diff_1x(),
            'grad_1x': self.get_grad_1x(),
            'diff_2x': self.get_diff_2x()
        }

    def get_massmat(self):
        """Mass-matrix.
        """

        data = np.array(
            [2.0, 1.0, 1.0, 2.0]
        )

        data = np.tile(
            data[..., None], (1, self.size)
        )

        data = data * (
            self.mesh.steps / 6.0
        )

        data = data.T.flatten()
        return VStream.from_data(data)

    def get_massdig(self):
        """Mass-matrix (lumped).
        """

        data = np.array(
            [0.5, 0.0, 0.0, 0.5]
        )

        data = np.tile(
            data[..., None], (1, self.size)
        )

        data = data * self.mesh.steps

        data = data.T.flatten()
        return VStream.from_data(data)

    def get_diff_1x(self):
        """1st derivative (weak).
        """

        data = np.array(
            [- 1.0, - 1.0, + 1.0, + 1.0]
        )

        data = np.tile(
            data[..., None], (1, self.size)
        )

        data = data * 0.5

        data = data.T.flatten()
        return VStream.from_data(data)

    def get_grad_1x(self):
        """1st derivative (strong).
        """

        data = np.array(
            [- 1.0, + 1.0, - 1.0, + 1.0]
        )

        data = np.tile(
            data[..., None], (1, self.size)
        )

        data = data * 0.5

        data = data.T.flatten()
        return VStream.from_data(data)

    def get_diff_2x(self):
        """2nd derivative (weak).
        """

        data = np.array(
            [1.0, - 1.0, - 1.0, 1.0]
        )

        data = np.tile(
            data[..., None], (1, self.size)
        )

        data = data / self.mesh.steps

        data = data.T.flatten()
        return VStream.from_data(data)


class VStream:
    """Stream of values.
    """

    def __init__(self, data):
        self.data = data

    @classmethod
    def from_data(cls, data):
        return cls(data)

    @property
    def size(self):
        return self.data.size
