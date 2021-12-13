import input_13
from aoc import advent_of_code


def print_board(board):
    for y in range(6):
        print()
        for x in range(39):
            if (x, y) in board:
                print("#", end=" ")
            else:
                print(".", end=" ")


def part_one(input):
    folds, dots = input

    board = set()
    for x, y in dots:
        board.add((x, y))

    fold_direction = folds[0]["direction"]
    fold_amount = folds[0]["amount"]
    new_board = perform_fold(board, fold_direction, fold_amount)

    return len(new_board)


def perform_fold(board, fold_direction, fold_amount):
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

    return new_board


def part_two(input):
    folds, dots = input

    board = set()
    for x, y in dots:
        board.add((x, y))

    for fold in folds:
        fold_direction = fold["direction"]
        fold_amount = fold["amount"]
        board = perform_fold(board, fold_direction, fold_amount)

    print_board(board)

    return len(board)


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

advent_of_code(
    {
        "day": 13,
        "part": 2,
        "fn": part_two,
        "sample": input_13.sample(),
        "expected": 16,
        "real": input_13.real(),
    }
)
