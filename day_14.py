import input_14
from aoc import advent_of_code
from collections import Counter


def apply_rules(input, times):
    template, insertion_rules = input

    pairs = Counter()
    letters = Counter()
    for a, b in zip(template, template[1:]):
        pairs[a + b] += 1
    for a in template:
        letters[a] += 1

    for _ in range(times):
        for (first_letter, last_letter), count in pairs.copy().items():
            new_letter = insertion_rules[first_letter + last_letter]
            pairs[first_letter + last_letter] -= count
            pairs[first_letter + new_letter] += count
            pairs[new_letter + last_letter] += count
            letters[new_letter] += count

    return letters.most_common()[0][1] - letters.most_common()[-1][1]


def part_one(input):
    return apply_rules(input, 10)


def part_two(input):
    return apply_rules(input, 40)


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


advent_of_code(
    {
        "day": 14,
        "part": 2,
        "fn": part_two,
        "sample": input_14.sample(),
        "expected": 2188189693529,
        "real": input_14.real(),
    }
)
