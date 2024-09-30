import matplotlib
import matplotlib.pyplot
import pytest

from mplstadium import Stadium3D

matplotlib.use("Agg")


@pytest.mark.mpl_image_compare(baseline_dir="baseline")
def test_stadium3d_draw():
    fig = matplotlib.pyplot.figure()
    ax = fig.add_subplot(111, projection="3d")

    stadium = Stadium3D(
        length=100,
        radius=10,
        width=10,
        straight_banking=10,
        curve_banking=20,
    )

    stadium.draw(ax, color="blue", edgecolor="white", alpha=0.5)

    assert isinstance(fig, matplotlib.figure.Figure)
    assert isinstance(ax, matplotlib.axes.Axes)

    ax.set_aspect("equal")
    return fig


@pytest.mark.mpl_image_compare(baseline_dir="baseline")
def test_stadium3d_scatter():
    stadium = Stadium3D(
        length=100,
        radius=10,
        width=10,
        straight_banking=10,
        curve_banking=20,
    )

    tangential = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    radial = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    fig, ax = stadium.draw(color="blue", edgecolor="white", alpha=0.5)

    stadium.scatter(tangential, radial, s=50, c="red", alpha=1)

    assert isinstance(fig, matplotlib.figure.Figure)
    assert isinstance(ax, matplotlib.axes.Axes)

    ax.set_aspect("equal")
    return fig


@pytest.mark.mpl_image_compare(baseline_dir="baseline")
def test_stadium3d_trajectory():
    stadium = Stadium3D(
        length=100,
        radius=10,
        width=10,
        straight_banking=10,
        curve_banking=20,
    )

    tangential = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    radial = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    fig, ax = stadium.draw(color="blue", edgecolor="white", alpha=0.5)

    stadium.trajectory(tangential, radial, c="red", lw=5, alpha=1)

    assert isinstance(fig, matplotlib.figure.Figure)
    assert isinstance(ax, matplotlib.axes.Axes)

    ax.set_aspect("equal")
    return fig
