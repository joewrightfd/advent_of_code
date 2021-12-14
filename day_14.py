import input_14
from aoc import advent_of_code
from collections import Counter


def expand_polymer(template, insertion_rules):
    new_version = []
    for a, b in zip(template, template[1:]):
        code = a + b
        new_letter = insertion_rules[code]
        new_version.append(new_letter)

    merged = []
    for i in range(len(template) + len(new_version)):
        relative_index = int(i / 2)
        if i % 2 == 1:
            merged.append(new_version[relative_index])
        else:
            merged.append(template[relative_index])

    return merged


def part_one(input):
    template, insertion_rules = input

    for _ in range(10):
        template = expand_polymer(template, insertion_rules)

    stuff = Counter(template).most_common()

    return stuff[0][1] - stuff[-1][1]


advent_of_code(
    {
        "day": 14,
        "part": 1,
        "fn": part_one,
        "sample": input_14.sample(),
        "expected": 1588,
        "real": input_14.real(),
    }
)
