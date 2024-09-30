import matplotlib
import matplotlib.pyplot
import pytest

from mplstadium import Stadium2D

matplotlib.use("Agg")

@pytest.mark.mpl_image_compare(baseline_dir="baseline")
def test_stadium2d_draw():
    fig, ax = matplotlib.pyplot.subplots()

    stadium = Stadium2D(
        length=100,
        radius=10,
        width=10,
        straight_banking=10,
        curve_banking=20,
        lane_widths=[10],
        lane_colors=["white", "white"],
        surface_color="blue",
        infield_width=2,
        infield_color="red",
    )

    stadium.draw(
        ax,
    )

    assert isinstance(fig, matplotlib.figure.Figure)
    assert isinstance(ax, matplotlib.axes.Axes)

    return fig

@pytest.mark.mpl_image_compare(baseline_dir="baseline")
def test_stadium2d_scatter():
    stadium = Stadium2D(
        length=100,
        radius=10,
        width=10,
        straight_banking=10,
        curve_banking=20,
        lane_widths=[10],
        lane_colors=["white", "white"],
        surface_color="blue",
        infield_width=2,
        infield_color="red",
    )

    tangential = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    radial = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    fig, ax = stadium.draw()

    stadium.scatter(tangential, radial, s=50, c="red")

    assert isinstance(fig, matplotlib.figure.Figure)
    assert isinstance(ax, matplotlib.axes.Axes)

    return fig


@pytest.mark.mpl_image_compare(baseline_dir="baseline")
def test_stadium2d_trajectory():
    stadium = Stadium2D(
        length=100,
        radius=10,
        width=10,
        straight_banking=10,
        curve_banking=20,
        lane_widths=[10],
        lane_colors=["white", "white"],
        surface_color="blue",
        infield_width=2,
        infield_color="red",
    )

    tangential = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    radial = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    fig, ax = stadium.draw()

    stadium.trajectory(tangential, radial, c="red", lw=5)

    assert isinstance(fig, matplotlib.figure.Figure)
    assert isinstance(ax, matplotlib.axes.Axes)

    return fig





