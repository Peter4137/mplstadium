**A Python plotting library to visualize stadium data**

# Quick start

Install the package using `pip` (or `pip3`).

```
pip install mplstadium
```

Plot an outdoor 400m running track, with the origin at the centre of the track:


```python
from mplstadium.utils import OutdoorAthleticsTrack2D
from matplotlib import pyplot as plt

track = OutdoorAthleticsTrack2D()
fig, ax = track.draw(line_kwargs={"color": "lightblue"}, fill_kwargs={"color": "blue"})
ax.set_aspect("equal")
plt.show()
```

<p align="center">
    <img src="https://github.com/Peter4137/mplstadium/blob/main/figs/outdoor_athletics_track.png?raw=true">
</p>

Plot an Olympic Velodrome in 3D and a trajectory on the surface:

```python
from mplstadium.utils import OlympicVelodrome3D
import numpy as np
from matplotlib import pyplot as plt

track = OlympicVelodrome3D()
fig, ax = track.draw(color="peru", alpha=0.5)

s = np.linspace(0, 250, 250)
d = 4 + 4 * np.sin(s / 10)

track.trajectory(s, d, c="r")

ax.set_aspect("equal")
ax.axis("off")
plt.show()
```

<p align="center">
  <img src="https://github.com/Peter4137/mplstadium/blob/main/figs/olympic_velodrome_3d_trajectory.png?raw=true" width="75%">
</p>

Define a custom Stadium geometry and plot scatter points over it:

```python
from mplstadium import Stadium3D
import numpy as np
from matplotlib import pyplot as plt

track = Stadium3D(
    length=500,
    radius=24.37,
    width=12,
    straight_banking=0,
    curve_banking=20,
)
fig, ax = track.draw(color="black", alpha=0.5)

s = np.linspace(0, 500, 50)
d = np.random.uniform(0, 12, 50)

track.scatter(s, d, c="r")

ax.set_aspect("equal")
ax.axis("off")
plt.show()
```

<p align="center">
  <img src="https://github.com/Peter4137/mplstadium/blob/main/figs/custom_stadium_scatter.png?raw=true" width="75%">
</p>

# License

[MIT](https://raw.githubusercontent.com/mlsedigital/mplbasketball/main/LICENSE.txt)