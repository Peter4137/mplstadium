from typing import Tuple

import matplotlib
import numpy as np
from matplotlib import pyplot as plt

from .stadium_base import StadiumBase


class Stadium2D(StadiumBase):
    """A class to represent a stadium-shaped track and facilitate plots of and on its surface in 2D.

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

    def _init_ax(self, ax: plt.Axes):
        self._ax = ax
        if self._ax is None:
            self._fig = plt.figure()
            self._ax = self._fig.add_subplot(111)

    def draw(
        self,
        ax: plt.Axes = None,
        line_args: list = None,
        line_kwargs: dict = None,
        fill_args: list = None,
        fill_kwargs: dict = None,
        s_points: int = 250,
        d_points: int = 9,
    ) -> Tuple[plt.Figure, plt.Axes]:
        """Plot the stadium in 2D.

        Parameters
        ----------
        ax : plt.Axes
            The axis to plot on.
        fill_color : str
            The color to fill the stadium with.
        fill_alpha : float
            The alpha value of the fill color.
        edge_color : str
            The color of the edges of the stadium.
        edge_alpha : float
            The alpha value of the edge color.
        s_points : int
            The number of points to use in the tangential direction.

        """
        assert d_points >= 2, "d_points must be at least 2"

        self._init_ax(ax)

        all_s = np.linspace(0, self.length, s_points)
        all_d = np.linspace(0, self.width, d_points)

        lines = [
            np.array([self._transform_xyz(s, d) for s in all_s]) for d in all_d
        ]

        for line in lines:
            self._ax.plot(line[:, 0], line[:, 1], *line_args or [], **line_kwargs)

        self._ax.fill(lines[-1][:, 0], lines[-1][:, 1], *fill_args or [], **fill_kwargs)
        self._ax.fill(lines[0][:, 0], lines[0][:, 1], color="white", alpha=1)


        if self._fig:
            return self._fig, self._ax
        else:
            return self._ax


    def trajectory(
        self,
        s_: np.ndarray,
        d_: np.ndarray,
        *args,
        **kwargs,
    ) -> matplotlib.lines.Line2D:
        """Plot a trajectory on the stadium.

        Parameters
        ----------
        s_ : np.ndarray
            The tangential position of the trajectory.
        d_ : np.ndarray
            The radial of the trajectory.
        args : list
            Additional positional arguments to pass to the plot
            function.
        kwargs : dict
            Additional keyword arguments to pass to the plot
            function.

        """
        points = np.array([
            self._transform_xyz(s_i, d_i) for s_i, d_i in zip(s_, d_)
        ])

        return self._ax.plot(points[:, 0], points[:, 1], *args, **kwargs)


    def scatter(
        self,
        s_: np.ndarray,
        d_: np.ndarray,
        *args,
        **kwargs,
    ) -> matplotlib.collections.PathCollection:
        """Scatter points on the stadium.

        Parameters
        ----------
        s_ : np.ndarray
            The tangential position of the points.
        d_ : np.ndarray
            The radial of the points.
        args : list
            Additional positional arguments to pass to the scatter
            function.
        kwargs : dict
            Additional keyword arguments to pass to the scatter
            function.

        """
        points = np.array([
            self._transform_xyz(s_i, d_i) for s_i, d_i in zip(s_, d_)
        ])

        return self._ax.scatter(points[:, 0], points[:, 1], *args, **kwargs)
