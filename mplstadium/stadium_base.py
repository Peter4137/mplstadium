import abc
from typing import Tuple

import numpy as np
from matplotlib import pyplot as plt


class StadiumBase(abc.ABC):
    """A base class to represent a stadium-shaped track and facilitate plots of and on its surface.

    Attributes:
    ----------
    length : float
        The length of the track.
    radius : float
        The radius of the track.
    width : float
        The width of the track.
    straight_banking : float
        The banking angle (deg) of the straight sections of the track.
    curve_banking : float
        The banking angle (deg) of the curved sections of the track.

    """

    def __init__(
        self,
        length: float,
        radius: float,
        width: float,
        straight_banking: float,
        curve_banking: float,
    ):
        self.length = length
        self.radius = radius
        self.width = width
        self.straight_banking = straight_banking
        self.curve_banking = curve_banking

        self._q_straight: float = (self.length - 2 * np.pi * self.radius) / 4
        self._ax: plt.Axes = None
        self._fig: plt.Figure = None

    def _banking(self, s) -> float:
        return np.pi * (
            ((self.straight_banking + self.curve_banking) / 2)
            - (self.curve_banking - self.straight_banking)/2 * np.cos(4 * (s / self.length) * np.pi)
        ) / 180

    def _transform_xyz(self, s, d) -> Tuple[float, float, float]:
        s = s % self.length
        banking_angle = self._banking(s)
        d_xy = d * np.cos(banking_angle)
        d_z = d * np.sin(banking_angle)
        if s < self._q_straight:
            return (
                s,
                -1 * (self.radius + d_xy),
                d_z
            )
        elif s < self._q_straight + np.pi * self.radius:
            angle = (s - self._q_straight) / self.radius
            return (
                self._q_straight + (self.radius + d_xy) * np.sin(angle),
                -1 * (self.radius + d_xy) * np.cos(angle),
                d_z
            )
        elif s < 3 * self._q_straight + np.pi * self.radius:
            return (
                2 * self._q_straight + np.pi * self.radius - s,
                self.radius + d_xy,
                d_z
            )
        elif s < 3 * self._q_straight + 2 * np.pi * self.radius:
            angle = (s - (3 * self._q_straight + np.pi * self.radius)) / self.radius
            return (
                -1 * self._q_straight - (self.radius + d_xy) * np.sin(angle),
                (self.radius + d_xy) * np.cos(angle),
                d_z
            )
        else:
            return (
                s - 4 * self._q_straight - 2 * np.pi * self.radius,
                -1 * (self.radius + d_xy),
                d_z
            )

    @abc.abstractmethod
    def _init_ax(self, ax: plt.Axes):
        pass

    @abc.abstractmethod
    def draw(self) -> Tuple[plt.Figure, plt.Axes]:
        pass

    @abc.abstractmethod
    def trajectory(self):
        pass

    @abc.abstractmethod
    def scatter(self):
        pass
