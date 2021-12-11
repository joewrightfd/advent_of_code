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


def to_completer_score(symbols):
    table = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4,
    }

    score = 0
    for symbol in symbols[::-1]:
        score *= 5
        score += table[symbol]

    return score


def part_two(input):
    incomplete_lines = []
    for line in input:
        good = True
        open_stack = []
        for char in line:
            if char in ["(", "{", "<", "["]:
                open_stack.append(char)

            if char == ")" and open_stack[-1] != "(":
                good = False
                break
            if char == "}" and open_stack[-1] != "{":
                good = False
                break
            if char == ">" and open_stack[-1] != "<":
                good = False
                break
            if char == "]" and open_stack[-1] != "[":
                good = False
                break

            if char in [")", "}", ">", "]"]:
                open_stack.pop()

        if good and len(open_stack) > 0:
            incomplete_lines.append(to_completer_score(open_stack))

    incomplete_lines.sort()
    middleIndex = int((len(incomplete_lines) - 1) / 2)
    return incomplete_lines[middleIndex]


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


advent_of_code(
    {
        "day": 10,
        "part": 2,
        "fn": part_two,
        "sample": input_10.sample(),
        "expected": 288957,
        "real": input_10.real(),
    }
)
