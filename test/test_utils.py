from mplstadium.utils import (
    IndoorAthleticsTrack2D,
    IndoorAthleticsTrack3D,
    OlympicVelodrome2D,
    OlympicVelodrome3D,
    OutdoorAthleticsTrack2D,
    OutdoorAthleticsTrack3D,
)


def test_olympic_velodrome():
    velodrome2d = OlympicVelodrome2D()
    velodrome3d = OlympicVelodrome3D()

    assert velodrome2d.length == 250
    assert velodrome2d.radius == 24.37
    assert velodrome2d.width == 8
    assert velodrome2d.straight_banking == 12
    assert velodrome2d.curve_banking == 45

    assert velodrome3d.length == 250
    assert velodrome3d.radius == 24.37
    assert velodrome3d.width == 8
    assert velodrome3d.straight_banking == 12
    assert velodrome3d.curve_banking == 45


def test_outdoor_athletics_track():
    track2d = OutdoorAthleticsTrack2D()
    track3d = OutdoorAthleticsTrack3D()

    assert track2d.length == 400
    assert track2d.radius == 36.5
    assert track2d.width == 10
    assert track2d.straight_banking == 0
    assert track2d.curve_banking == 0

    assert track3d.length == 400
    assert track3d.radius == 36.5
    assert track3d.width == 10
    assert track3d.straight_banking == 0
    assert track3d.curve_banking == 0


def test_indoor_athletics_track():
    track2d = IndoorAthleticsTrack2D()
    track3d = IndoorAthleticsTrack3D()

    assert track2d.length == 200
    assert track2d.radius == 18.5
    assert track2d.width == 7.5
    assert track2d.straight_banking == 0
    assert track2d.curve_banking == 10

    assert track3d.length == 200
    assert track3d.radius == 18.5
    assert track3d.width == 7.5
    assert track3d.straight_banking == 0
    assert track3d.curve_banking == 10
