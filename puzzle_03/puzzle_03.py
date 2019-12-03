from collections import namedtuple

Point = namedtuple("Point", "x, y")


def add(self, other):
    return Point(self.x + other.x, self.y + other.y)


Point.__add__ = add


DIRECTION_DICT = {
    "U": Point(0, 1),
    "D": Point(0, -1),
    "L": Point(-1, 0),
    "R": Point(1, 0),
}


def points_from_path(path):
    position = Point(0, 0)
    path_points = [position]
    for move in path:
        direction, distance = DIRECTION_DICT[move[0]], int(move[1:])
        for _ in range(distance):
            position = position + direction
            path_points.append(position)
    return path_points


def min_crossing_distance_from_points(path_points1, path_points2):
    crossing_points = set(path_points1).intersection(set(path_points2))
    crossing_points.remove(Point(0, 0))
    manhatten_distances = set(abs(point.x) + abs(point.y) for point in crossing_points)
    return min(manhatten_distances)


def min_crossing_point_distance(path1, path2):
    return min_crossing_distance_from_points(
        points_from_path(path1.split(",")), points_from_path(path2.split(","))
    )


def min_crossing_distance_along_paths_from_points(path_points1, path_points2):
    crossing_points = set(path_points1).intersection(set(path_points2))
    crossing_points.remove(Point(0, 0))
    return min(
        path_points1.index(cp) + path_points2.index(cp) for cp in crossing_points
    )


def min_crossing_distance_along_paths(path1, path2):
    return min_crossing_distance_along_paths_from_points(
        points_from_path(path1.split(",")), points_from_path(path2.split(","))
    )


def read_input():
    with open("input.txt", "r") as stream:
        path1 = stream.readline()
        path2 = stream.readline()
    return path1, path2


def solve_part_1():
    return min_crossing_point_distance(*read_input())


def solve_part_2():
    return min_crossing_distance_along_paths(*read_input())


if __name__ == "__main__":
    print(f"Part 1: {solve_part_1()}")
    print(f"Part 2: {solve_part_2()}")
