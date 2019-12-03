import pytest
from puzzle_03 import Point, points_from_path, min_crossing_point_distance


def test_points_from_path():
    assert tuple(points_from_path(["U2", "R1", "D1"])) == (
        Point(0, 1),
        Point(0, 2),
        Point(1, 2),
        Point(1, 1),
    )


@pytest.mark.parametrize(
    "path1, path2, distance",
    [
        ("R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83", 159),
        (
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
            135,
        ),
    ],
)
def test_cde(path1, path2, distance):
    assert min_crossing_point_distance(path1, path2) == distance
