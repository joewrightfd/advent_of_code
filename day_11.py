import input_11
from aoc import advent_of_code

FLASH_ENERGY_LEVEL = 9


def neighbouring_cells(x, y, x_height, y_height):
    neighbours = [
        [x, y + 1],
        [x - 1, y + 1],
        [x + 1, y + 1],
        [x - 1, y],
        [x + 1, y],
        [x, y - 1],
        [x - 1, y - 1],
        [x + 1, y - 1],
    ]

    def in_bounds(cord):
        x, y = cord
        return y >= 0 and x >= 0 and y < y_height and x < x_height

    return filter(in_bounds, neighbours)


def increment(x, y, input, flashed_this_round):
    input[y][x] += 1
    if input[y][x] > FLASH_ENERGY_LEVEL and [x, y] not in flashed_this_round:
        flashed_this_round.append([x, y])
        for x, y in neighbouring_cells(x, y, len(input[y]), len(input)):
            increment(x, y, input, flashed_this_round)


def increment_grid(input):
    flashed_this_round = []

    for y in range(len(input)):
        for x in range(len(input[y])):
            increment(x, y, input, flashed_this_round)

    for x, y in flashed_this_round:
        input[y][x] = 0

    return len(flashed_this_round)


def part_one(input):
    return sum([increment_grid(input) for _ in range(1, 101)])


def part_two(input):
    for step in range(1, 400):
        increment_grid(input)
        if all(all(cell == 0 for cell in line) for line in input):
            return step

    return 0


advent_of_code(
    {
        "day": 11,
        "part": 1,
        "fn": part_one,
        "sample": input_11.sample(),
        "expected": 1656,
        "real": input_11.real(),
    }
)

advent_of_code(
    {
        "day": 11,
        "part": 2,
        "fn": part_two,
        "sample": input_11.sample(),
        "expected": 195,
        "real": input_11.real(),
    }
)
