import input_4
from aoc import advent_of_code


def transpose(list):
    # totes stolen: https://www.programiz.com/python-programming/examples/transpose-matrix
    return [[list[j][i] for j in range(len(list))] for i in range(len(list[0]))]


def flatten(t):
    return [item for sublist in t for item in sublist]


class Board:
    def __init__(self, state):
        self.rows = state
        self.cols = transpose(state)
        self.all_numbers = flatten(state)

    def wins_with(self, balls):
        for line in self.rows + self.cols:
            if all(number in balls for number in line):
                return True

        return False

    def unmarked_score(self, balls):
        return sum(filter(lambda number: number not in balls, self.all_numbers))


def part_one(input):
    balls, boards = input
    obj_boards = list(map(Board, boards))

    for idx in range(len(balls)):
        drawn = balls[0 : idx + 1]
        for board in obj_boards:
            if board.wins_with(drawn):
                return board.unmarked_score(drawn) * drawn[-1]

    return 0


def part_two(input):
    balls, boards = input
    obj_boards = list(map(Board, boards))
    remaining = obj_boards

    for idx in range(len(balls)):
        drawn = balls[0 : idx + 1]
        boards_left = list(filter(lambda b: not b.wins_with(drawn), remaining))
        if len(boards_left) == 0:
            return remaining[0].unmarked_score(drawn) * drawn[-1]
        remaining = boards_left

    return 0


advent_of_code(
    {
        "day": 4,
        "part": 1,
        "fn": part_one,
        "real": (input_4.real_balls(), input_4.real_boards()),
        "sample": (input_4.sample_balls(), input_4.sample_boards()),
        "expected": 4512,
    }
)

advent_of_code(
    {
        "day": 4,
        "part": 2,
        "fn": part_two,
        "real": (input_4.real_balls(), input_4.real_boards()),
        "sample": (input_4.sample_balls(), input_4.sample_boards()),
        "expected": 1924,
    }
)
