import input_9
from aoc import advent_of_code
import math


def neighbouring_cells(x, y, x_height, y_height):
    neighbours = [
        [x, y + 1],
        [x, y - 1],
        [x - 1, y],
        [x + 1, y],
    ]

    def in_bounds(cord):
        x, y = cord
        return y >= 0 and x >= 0 and y < y_height and x < x_height

    return list(filter(in_bounds, neighbours))


def find_lowest_points(input):
    x_height = len(input[0])
    y_height = len(input)

    lowest_points = []

    for y in range(y_height):
        for x in range(x_height):
            cell = input[y][x]

            a = neighbouring_cells(x, y, x_height, y_height)
            neighbours = map(lambda c: input[c[1]][c[0]], a)

            if cell < min(neighbours):
                lowest_points.append([x, y])

    return lowest_points


def part_one(input):
    lowest_points = find_lowest_points(input)
    return sum(map(lambda c: input[c[1]][c[0]] + 1, lowest_points))


def part_two(input):
    x_height = len(input[0])
    y_height = len(input)
    lowest_points = find_lowest_points(input)

    basin_sizes = []
    for lp in lowest_points:
        x, y = lp
        known = [lp]
        cells_to_visit = neighbouring_cells(x, y, x_height, y_height)
        for nx, ny in cells_to_visit:
            if [nx, ny] not in known and input[ny][nx] != 9:
                known.append([nx, ny])
                cells_to_visit.extend(neighbouring_cells(nx, ny, x_height, y_height))

        basin_sizes.append(len(known))

    basin_sizes.sort(reverse=True)
    return math.prod(basin_sizes[0:3])


advent_of_code(
    {
        "day": 9,
        "part": 1,
        "fn": part_one,
        "sample": input_9.sample(),
        "expected": 15,
        "real": input_9.real(),
    }
)

advent_of_code(
    {
        "day": 9,
        "part": 2,
        "fn": part_two,
        "sample": input_9.sample(),
        "expected": 1134,
        "real": input_9.real(),
    }
)
