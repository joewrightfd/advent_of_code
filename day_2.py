import input_2

from aoc import advent_of_code


def part_one(input):
    horizontal_pos = 0
    depth_pos = 0

    for direction, amount in input:
        if direction == "forward":
            horizontal_pos += amount
        if direction == "down":
            depth_pos += amount
        if direction == "up":
            depth_pos -= amount

    return horizontal_pos * depth_pos


def part_two(input):
    horizontal_pos = 0
    depth_pos = 0
    aim = 0

    for direction, amount in input:
        if direction == "forward":
            horizontal_pos += amount
            depth_pos += aim * amount
        if direction == "down":
            aim += amount
        if direction == "up":
            aim -= amount

    return horizontal_pos * depth_pos


advent_of_code(
    {
        "day": 2,
        "part": 1,
        "fn": part_one,
        "sample": input_2.sample(),
        "expected": 150,
        "real": input_2.input(),
    }
)

advent_of_code(
    {
        "day": 2,
        "part": 2,
        "fn": part_two,
        "sample": input_2.sample(),
        "expected": 900,
        "real": input_2.input(),
    }
)
