import input_1
from aoc import advent_of_code


def part_one(data):
    count = 0
    for a, b in zip(data, data[1:]):
        if a < b:
            count += 1
    return count


def part_two(data):
    count = 0
    for a, b, c, d in zip(data, data[1:], data[2:], data[3:]):
        if a + b + c < b + c + d:
            count += 1
    return count


advent_of_code(
    {
        "day": 1,
        "part": 1,
        "fn": part_one,
        "real": input_1.real(),
        "sample": input_1.sample(),
        "expected": 7,
    }
)

advent_of_code(
    {
        "day": 1,
        "part": 2,
        "fn": part_two,
        "real": input_1.real(),
        "sample": input_1.sample(),
        "expected": 5,
    }
)
