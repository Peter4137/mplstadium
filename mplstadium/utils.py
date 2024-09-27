from .stadium2d import Stadium2D
from .stadium3d import Stadium3D


class OlympicVelodrome2D(Stadium2D):
    def __init__(self):
        super().__init__(
            length=250,
            radius=24.37,
            width=8,
            straight_banking=12,
            curve_banking=45,
        )

class OlympicVelodrome3D(Stadium3D):
    def __init__(self):
        super().__init__(
            length=250,
            radius=24.37,
            width=8,
            straight_banking=12,
            curve_banking=45,
        )

class OutdoorAthleticsTrack2D(Stadium2D):
    def __init__(self):
        super().__init__(
            length=400,
            radius=36.5,
            width=8,
            straight_banking=0,
            curve_banking=0,
        )

class OutdoorAthleticsTrack3D(Stadium3D):
    def __init__(self):
        super().__init__(
            length=400,
            radius=36.5,
            width=8,
            straight_banking=0,
            curve_banking=0,
        )

class IndoorAthleticsTrack2D(Stadium2D):
    def __init__(self):
        super().__init__(
            length=200,
            radius=18.5,
            width=8,
            straight_banking=0,
            curve_banking=10,
        )

class IndoorAthleticsTrack3D(Stadium3D):
    def __init__(self):
        super().__init__(
            length=200,
            radius=18.5,
            width=8,
            straight_banking=0,
            curve_banking=10,
        )
