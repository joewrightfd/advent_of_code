import input_10
from aoc import advent_of_code
from pprint import pprint


def to_score(symbol):
    table = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    return table[symbol]


def part_one(input):
    broken_bits = []

    for line in input:
        open_stack = []
        for char in line:
            if char in ["(", "{", "<", "["]:
                open_stack.append(char)

            if char == ")" and open_stack[-1] != "(":
                broken_bits.append(")")
                break
            if char == "}" and open_stack[-1] != "{":
                broken_bits.append("}")
                break
            if char == ">" and open_stack[-1] != "<":
                broken_bits.append(">")
                break
            if char == "]" and open_stack[-1] != "[":
                broken_bits.append("]")
                break

            if char in [")", "}", ">", "]"]:
                open_stack.pop()

    return sum(map(to_score, broken_bits))


advent_of_code(
    {
        "day": 10,
        "part": 1,
        "fn": part_one,
        "sample": input_10.sample(),
        "expected": 26397,
        "real": input_10.real(),
    }
)
