import input_8
from aoc import advent_of_code
from collections import defaultdict, Counter


def part_one(input):
    # 0=6, 1=2, 2=5, 3=5, 4=4, 5=5, 6=6, 7=3, 8=7, 9=6
    count = 0

    for signal_patterns, output_values in input:
        lengths = map(len, output_values)
        count += len(list(filter(lambda x: x in [2, 3, 4, 7], lengths)))

    return count


def flatten(list):
    return [item for sublist in list for item in sublist]


# letters a-g
# top, mid, bottom, left-upper, left-lower, right-upper, right-lower
def part_two(input):
    count = 0

    for signal_patterns, output_values in input:
        symbols = defaultdict(list)
        for pattern in signal_patterns:
            symbols[len(pattern)].append(set(pattern))

        one_bits = symbols[2][0]
        four_bits = symbols[4][0]
        seven_bits = symbols[3][0]
        eight_bits = symbols[7][0]

        # first pass
        top_letter = list(seven_bits - one_bits)[0]
        left_upper_letter = set(four_bits - one_bits)
        right_upper_letter = one_bits
        mid_letter = set(four_bits - one_bits)
        left_lower_letter = eight_bits - set(top_letter) - one_bits
        right_lower_letter = one_bits
        bottom_letter = eight_bits - set(top_letter) - one_bits

        # second pass
        # zero, six, nine -> one of the left_upper two choices must appear 3 times to be correct
        left_upper_letter = Counter(
            filter(lambda x: x in left_upper_letter, flatten(symbols[6]))
        ).most_common(1)[0][0]

        # zero, six, nine -> one of the right_lower two choices must appear 3 times to be correct
        right_lower_letter = Counter(
            filter(lambda x: x in right_lower_letter, flatten(symbols[6]))
        ).most_common(1)[0][0]

        right_upper_letter = list(right_upper_letter - set(right_lower_letter))[0]
        mid_letter = list(mid_letter - set(left_upper_letter))[0]
        left_lower_letter = set(
            left_lower_letter - {left_upper_letter, mid_letter, right_lower_letter}
        )
        bottom_letter = set(
            bottom_letter - {left_upper_letter, mid_letter, right_lower_letter}
        )

        # third pass
        # zero, six, nine -> one of the right_lower two choices must appear 3 times to be correct
        bottom_letter = Counter(
            filter(lambda x: x in bottom_letter, flatten(symbols[6]))
        ).most_common(1)[0][0]

        left_lower_letter = list(left_lower_letter - set(bottom_letter))[0]

        bits_for_0 = {
            top_letter,
            left_upper_letter,
            right_upper_letter,
            left_lower_letter,
            right_lower_letter,
            bottom_letter,
        }
        bits_for_1 = {right_upper_letter, right_lower_letter}
        bits_for_2 = {
            top_letter,
            right_upper_letter,
            mid_letter,
            left_lower_letter,
            bottom_letter,
        }
        bits_for_3 = {
            top_letter,
            right_upper_letter,
            mid_letter,
            right_lower_letter,
            bottom_letter,
        }
        bits_for_4 = {
            left_upper_letter,
            mid_letter,
            right_upper_letter,
            right_lower_letter,
        }
        bits_for_5 = {
            top_letter,
            left_upper_letter,
            mid_letter,
            right_lower_letter,
            bottom_letter,
        }
        bits_for_6 = {
            top_letter,
            left_upper_letter,
            mid_letter,
            left_lower_letter,
            right_lower_letter,
            bottom_letter,
        }
        bits_for_7 = {top_letter, right_upper_letter, right_lower_letter}
        bits_for_8 = {
            top_letter,
            left_upper_letter,
            right_upper_letter,
            mid_letter,
            left_lower_letter,
            right_lower_letter,
            bottom_letter,
        }
        bits_for_9 = {
            top_letter,
            left_upper_letter,
            right_upper_letter,
            mid_letter,
            right_lower_letter,
            bottom_letter,
        }

        number = ""
        for value in output_values:
            if set(value) == bits_for_0:
                number += "0"
            if set(value) == bits_for_1:
                number += "1"
            if set(value) == bits_for_2:
                number += "2"
            if set(value) == bits_for_3:
                number += "3"
            if set(value) == bits_for_4:
                number += "4"
            if set(value) == bits_for_5:
                number += "5"
            if set(value) == bits_for_6:
                number += "6"
            if set(value) == bits_for_7:
                number += "7"
            if set(value) == bits_for_8:
                number += "8"
            if set(value) == bits_for_9:
                number += "9"

        count += int(number)

    return count


advent_of_code(
    {
        "day": 8,
        "part": 1,
        "fn": part_one,
        "sample": input_8.sample(),
        "expected": 26,
        "real": input_8.real(),
    }
)

advent_of_code(
    {
        "day": 8,
        "part": 2,
        "fn": part_two,
        "sample": input_8.sample(),
        "expected": 61229,
        "real": input_8.real(),
    }
)
