import input_8
from aoc import advent_of_code
from collections import defaultdict, Counter


def part_one(input):
    count = 0

    for _, output_values in input:
        lengths = map(len, output_values)
        count += len(list(filter(lambda x: x in [2, 3, 4, 7], lengths)))

    return count


def flatten(list):
    return [item for sublist in list for item in sublist]


def part_two(input):
    count = 0

    for signal_patterns, output_values in input:
        symbols_by_length = defaultdict(list)
        for pattern in signal_patterns:
            symbols_by_length[len(pattern)].append(set(pattern))
        t = LettersAndPositions(symbols_by_length)

        # Perform sodoku given what we know
        t.is_definitely("top", t.letters[7] - t.letters[1])
        t.is_the_most_common_within(
            "left_upper",
            t.letters[4] - t.letters[1],  # -> left_upper, mid
            t.letters["0,6,9"],  # mid is not in 0
        )
        t.is_definitely(
            "mid",
            t.letters[4] - t.letters[1] - set(t.at["left_upper"]),
        )
        t.is_the_most_common_within(
            "right_lower",
            t.letters[1],  # -> right_upper, right_lower
            t.letters["0,6,9"],  # right_upper is not in 6
        )
        t.is_definitely(
            "right_upper",
            t.letters[1] - set(t.at["right_lower"]),
        )
        t.is_the_most_common_within(
            "bottom",
            t.letters[8] - t.letters[7] - t.letters[4],  # -> left_lower, bottom
            t.letters["0,6,9"],  # left_lower is not in 9
        )
        t.is_definitely(
            "left_lower",
            t.letters[8] - t.letters[7] - t.letters[4] - {t.at["bottom"]},
        )

        # Figure out the six unknown numbers now we have the pattern
        t.letters[0] = next(filter(lambda x: t.at["mid"] not in x, t.letters["0,6,9"]))
        t.letters[6] = next(
            filter(lambda x: t.at["right_upper"] not in x, t.letters["0,6,9"])
        )
        t.letters[9] = next(
            filter(lambda x: t.at["left_lower"] not in x, t.letters["0,6,9"])
        )
        t.letters[2] = next(
            filter(
                lambda x: t.at["right_upper"] in x and t.at["left_lower"] in x,
                t.letters["2,3,5"],
            )
        )
        t.letters[3] = next(
            filter(
                lambda x: t.at["right_upper"] in x and t.at["right_lower"] in x,
                t.letters["2,3,5"],
            )
        )
        t.letters[5] = next(
            filter(
                lambda x: t.at["left_upper"] in x and t.at["right_lower"] in x,
                t.letters["2,3,5"],
            )
        )

        digits = ""
        for value in output_values:
            digits += t.output_to_digit(value)

        count += int(digits)

    return count


class LettersAndPositions:
    def __init__(self, symbols_by_length):
        self.letters = {
            1: symbols_by_length[2][0],
            4: symbols_by_length[4][0],
            7: symbols_by_length[3][0],
            8: symbols_by_length[7][0],
            "0,6,9": symbols_by_length[6],
            "2,3,5": symbols_by_length[5],
        }

        self.at = {}

    def is_definitely(self, position, letter):
        self.at[position] = list(letter)[0]

    def is_the_most_common_within(self, position, possible, letters):
        always_present = Counter(
            filter(lambda x: x in possible, flatten(letters))
        ).most_common(1)
        self.is_definitely(position, always_present[0])

    def output_to_digit(self, value):
        for number, letters in self.letters.items():
            if set(value) == letters:
                return f"{number}"

        return ""


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
