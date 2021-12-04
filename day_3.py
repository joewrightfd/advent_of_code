import input_3
from aoc import advent_of_code

from collections import Counter


def transpose(list):
    # totes stolen: https://www.programiz.com/python-programming/examples/transpose-matrix
    return [[list[j][i] for j in range(len(list))] for i in range(len(list[0]))]


def most_common(list):
    c = Counter(list).most_common()

    if len(c) == 2 and c[0][1] == c[1][1]:
        return 1

    return c[0][0]


def least_common(list):
    c = Counter(list).most_common()

    if len(c) == 2 and c[0][1] == c[1][1]:
        return 0

    return c[-1][0]


def list_of_ints_to_single_number(list):
    s = [str(i) for i in list]
    res = "".join(s)
    return res


def frequent_number_in_list(list2, finder_fn):
    most_common_per_column = list(map(finder_fn, list2))
    binary = list_of_ints_to_single_number(most_common_per_column)
    return int(binary, 2)


def part_one(input):
    by_column = transpose(input)
    gamma_number = frequent_number_in_list(by_column, most_common)
    epsilon_number = frequent_number_in_list(by_column, least_common)
    answer = gamma_number * epsilon_number

    return {
        "gamma": gamma_number,
        "epsilon": epsilon_number,
        "result": answer,
    }


def apply_part_two_logic(input, common_fn):
    remaining = input
    for idx in range(len(input[0])):
        nths = [e[idx] for e in remaining]
        winner = common_fn(nths)
        remaining = list(filter(lambda x: x[idx] == winner, remaining))

    return remaining[0]


def part_two(input):
    og_remaining = apply_part_two_logic(input, most_common)
    oxygen_generator_rating_binary = list_of_ints_to_single_number(og_remaining)
    oxygen_generator_rating = int(oxygen_generator_rating_binary, 2)

    c02_remaining = apply_part_two_logic(input, least_common)
    co2_binary = list_of_ints_to_single_number(c02_remaining)
    co2 = int(co2_binary, 2)

    life_support_rating = oxygen_generator_rating * co2
    return {"ox": oxygen_generator_rating, "co2": co2, "result": life_support_rating}


advent_of_code(
    {
        "day": 3,
        "part": 1,
        "fn": part_one,
        "sample": input_3.sample(),
        "expected": {
            "gamma": 22,
            "epsilon": 9,
            "result": 198,
        },
        "real": input_3.real(),
    }
)

advent_of_code(
    {
        "day": 3,
        "part": 2,
        "fn": part_two,
        "sample": input_3.sample(),
        "expected": {"ox": 23, "co2": 10, "result": 230},
        "real": input_3.real(),
    }
)
