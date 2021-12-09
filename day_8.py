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
        symbols = defaultdict(list)
        for pattern in signal_patterns:
            symbols[len(pattern)].append(set(pattern))

        t = LettersAndSymbols(symbols)

        t.is_definitely("top", t.known_letters[7] - t.known_letters[1])

        t.is_the_most_common_within(
            "left_upper",
            t.known_letters[4] - t.known_letters[1],
            t.unknown_letters["0,6,9"],
        )

        t.is_definitely(
            "mid",
            t.known_letters[4] - t.known_letters[1] - set(t.at["left_upper"]),
        )

        t.is_the_most_common_within(
            "right_lower", t.known_letters[1], t.unknown_letters["0,6,9"]
        )

        t.is_definitely(
            "right_upper",
            t.known_letters[1] - set(t.at["right_lower"]),
        )

        t.is_the_most_common_within(
            "bottom",
            t.known_letters[8] - t.known_letters[7] - t.known_letters[4],
            t.unknown_letters["0,6,9"],
        )

        t.is_definitely(
            "left_lower",
            t.known_letters[8]
            - t.known_letters[7]
            - t.known_letters[4]
            - {t.at["bottom"]},
        )

        # figure out which is a 0, 6 or 9
        t.known_letters[0] = next(
            filter(lambda x: t.at["mid"] not in x, t.unknown_letters["0,6,9"])
        )
        t.known_letters[6] = next(
            filter(lambda x: t.at["right_upper"] not in x, t.unknown_letters["0,6,9"])
        )
        t.known_letters[9] = next(
            filter(lambda x: t.at["left_lower"] not in x, t.unknown_letters["0,6,9"])
        )

        # figure out which is a 2,3,5 - they all have top,mid.bottom
        t.known_letters[2] = next(
            filter(
                lambda x: t.at["right_upper"] in x and t.at["left_lower"] in x,
                t.unknown_letters["2,3,5"],
            )
        )
        t.known_letters[3] = next(
            filter(
                lambda x: t.at["right_upper"] in x and t.at["right_lower"] in x,
                t.unknown_letters["2,3,5"],
            )
        )
        t.known_letters[5] = next(
            filter(
                lambda x: t.at["left_upper"] in x and t.at["right_lower"] in x,
                t.unknown_letters["2,3,5"],
            )
        )

        digits = ""
        for value in output_values:
            digits += t.output_to_digit(value)

        count += int(digits)

    return count


class LettersAndSymbols:
    def __init__(self, symbols):
        self.known_letters = {
            1: symbols[2][0],
            4: symbols[4][0],
            7: symbols[3][0],
            8: symbols[7][0],
        }
        self.unknown_letters = {"0,6,9": symbols[6], "2,3,5": symbols[5]}

        self.at = {}

    def is_definitely(self, position, letter):
        self.at[position] = list(letter)[0]

    def is_the_most_common_within(self, position, possible, letters):
        always_present = Counter(
            filter(lambda x: x in possible, flatten(letters))
        ).most_common(1)

        self.is_definitely(position, always_present[0])

    def output_to_digit(self, value):
        for number, letters in self.known_letters.items():
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
