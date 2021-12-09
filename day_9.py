import input_9
from aoc import advent_of_code


def part_one(input):
    x_height = len(input[0])
    y_height = len(input)

    lowest_points = []

    for y in range(y_height):
        for x in range(x_height):
            cell = input[y][x]
            neighbours = []

            if y > 0 and y < y_height:
                neighbours.append(input[y - 1][x])
            if y < (y_height - 1):
                neighbours.append(input[y + 1][x])
            if x > 0 and x < x_height:
                neighbours.append(input[y][x - 1])
            if x < (x_height - 1):
                neighbours.append(input[y][x + 1])

            if cell < min(neighbours):
                lowest_points.append(cell)

    return sum(map(lambda x: x + 1, lowest_points))


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
