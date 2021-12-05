import input_5
from aoc import advent_of_code
from collections import Counter


def vertical_cords(y1, y2, x):
    cords = []
    for offset in range(max(y1, y2) - min(y1, y2) + 1):
        y = min(y1, y2) + offset
        cords.append(f"{x},{y}")
    return cords


def horizontal_cords(x1, x2, y):
    cords = []
    for offset in range(max(x1, x2) - min(x1, x2) + 1):
        x = min(x1, x2) + offset
        cords.append(f"{x},{y}")
    return cords


def diagonal_cords(x1, y1, x2, y2):
    cords = []
    x_mod = -1 if x1 > x2 else 1
    y_mod = -1 if y1 > y2 else 1
    for offset in range(abs(x1 - x2) + 1):
        x = x1 + (offset * x_mod)
        y = y1 + (offset * y_mod)
        cords.append(f"{x},{y}")
    return cords


def duplicate_items(lst):
    freq = Counter(lst).most_common()
    return list(filter(lambda x: x[1] > 1, freq))


def part_one(input):
    cords = []
    for start, end in input:
        x1, y1 = start
        x2, y2 = end

        if x1 == x2:
            cords += vertical_cords(y1, y2, x1)

        if y1 == y2:
            cords += horizontal_cords(x1, x2, y1)

    return len(duplicate_items(cords))


def part_two(input):
    cords = []
    for start, end in input:
        x1, y1 = start
        x2, y2 = end

        if x1 == x2:
            cords += vertical_cords(y1, y2, x1)

        if y1 == y2:
            cords += horizontal_cords(x1, x2, y1)

        if abs(x1 - x2) == abs(y1 - y2):
            cords += diagonal_cords(x1, y1, x2, y2)

    return len(duplicate_items(cords))


advent_of_code(
    {
        "day": 5,
        "part": 1,
        "fn": part_one,
        "sample": input_5.sample(),
        "expected": 5,
        "real": input_5.real(),
    }
)

advent_of_code(
    {
        "day": 5,
        "part": 2,
        "fn": part_two,
        "sample": input_5.sample(),
        "expected": 12,
        "real": input_5.real(),
    }
)
