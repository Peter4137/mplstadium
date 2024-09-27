from .stadium_base import StadiumBase
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib

class Stadium3D(StadiumBase):

    """
    A class to represent a stadium-shaped track and facilitate plots of and on its surface in 3D.

    Attributes
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
        
    def _init_ax(self, ax: Axes3D):
        self._ax = ax
        if self._ax is None:
            self._fig = plt.figure()
            self._ax = self._fig.add_subplot(111, projection="3d")

    def draw(
        self,
        ax: plt.Axes = None,
        s_points: int = 250,
        d_points: int = 10,
        *args,
        **kwargs,
    ) -> tuple[plt.Figure, Axes3D]:
        """
        Plot the stadium in 3D.
        
        Parameters
        ----------
        ax : plt.Axes
            The axis to plot on.
        s_points : int
            The number of points to use in the tangential direction.
        d_points : int
            The number of points to use in the radial direction.
        args: list
            Additional positional arguments to pass to the plot
            function.
        kwargs: dict
            Additional keyword arguments to pass to the plot
            function.

        """
        assert d_points >= 2, "d_points must be at least 2"

        self._init_ax(ax)

        s = np.linspace(0, self.length, s_points)
        d = np.linspace(0, self.width, d_points)

        points = np.array([
            [self._transform_xyz(s_, d_) for s_ in s] for d_ in d
        ])

        self._ax.plot_surface(
            points[:,:,0], 
            points[:,:,1], 
            points[:,:,2], 
            *args,
            **kwargs,
        )

        if self._fig:
            return self._fig, self._ax
        else:
            return self._ax
    
    def trajectory(
        self,
        s_: np.ndarray,
        d: np.ndarray,
        *args,
        **kwargs,
    ) -> matplotlib.lines.Line2D:
        """
        Plot a trajectory on the stadium.
        
        Parameters
        ----------
        s : np.ndarray
            The tangential position of the trajectory.
        d : np.ndarray
            The radial of the trajectory.
        args : list
            Additional positional arguments to pass to the plot
            function.
        kwargs : dict
            Additional keyword arguments to pass to the plot
            function.
        
        """
        points = np.array([
            self._transform_xyz(s_i, d_i) for s_i, d_i in zip(s_, d)
        ])

        return self._ax.plot(points[:, 0], points[:, 1], points[:, 2], *args, **kwargs)

    def scatter(
        self,
        s_: np.ndarray,
        d_: np.ndarray,
        *args,
        **kwargs,
    ) -> matplotlib.collections.PathCollection:
        """
        Scatter points on the stadium.

        Parameters
        ----------
        s : np.ndarray
            The tangential position of the points.
        d : np.ndarray
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

        return self._ax.scatter(points[:, 0], points[:, 1], points[:, 2], *args, **kwargs)
