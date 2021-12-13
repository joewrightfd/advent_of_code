import input_13
from aoc import advent_of_code


def part_one(input):
    folds, dots = input
    fold_direction = folds[0]["direction"]
    fold_amount = folds[0]["amount"]

    board = set()
    for x, y in dots:
        board.add((x, y))

    new_board = set()
    for x, y in board:
        if y > fold_amount and fold_direction == "y":
            moved_by = y - fold_amount
            new_board.add((x, fold_amount - moved_by))
        elif x > fold_amount and fold_direction == "x":
            moved_by = x - fold_amount
            new_board.add((fold_amount - moved_by, y))
        else:
            new_board.add((x, y))

    return len(new_board)


advent_of_code(
    {
        "day": 13,
        "part": 1,
        "fn": part_one,
        "sample": input_13.sample(),
        "expected": 17,
        "real": input_13.real(),
    }
)
