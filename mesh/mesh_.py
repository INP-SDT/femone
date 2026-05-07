# -*- coding: utf-8 -*-
"""Mesh object.
"""
import numpy as np


def getmesh(points):
    """Creates a mesh object.

    Parameters
    ----------
    points : flat-float-array
        Input points.

    Returns
    -------
    Mesh
        Mesh object.

    """
    return Mesh.from_points(points)


class Mesh:
    """Mesh object.

    Properties
    ----------

    Name      |  Description
    ----------|---------------------------
    `steps`   | Element sizes
    `centrs`  | Element midpoints

    """

    def __init__(self, points, elements):
        self.points = points
        self.elements = elements

    @classmethod
    def from_points(cls, points):
        return cls(
            points, getelements(len(points))
        )

    @property
    def size(self):
        return self.points.size

    @property
    def steps(self):
        return np.diff(self.points)

    @property
    def centrs(self):
        return 0.5 * (
            self.points[:-1] + self.points[1::]
        )


def getelements(count):

    elements = np.array(
        [np.arange(0, count - 1), np.arange(1, count + 0)]
    )

    return elements.T.copy()
