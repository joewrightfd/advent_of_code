import input_7
from aoc import advent_of_code


def part_one(input):
    distances = {}
    for i in range(min(input), max(input)):
        distances[i] = sum(map(lambda x: abs(x - i), input))

    return min(distances.values())


advent_of_code(
    {
        "day": 7,
        "part": 1,
        "fn": part_one,
        "sample": input_7.sample(),
        "expected": 37,
        "real": input_7.real(),
    }
)
