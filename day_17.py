from aoc import advent_of_code


def triangular_number(n):
    return int(n * (n + 1) / 2)


def passes_through_target(trajectory, target):
    current_pos = (0, 0)
    current_trajectory = trajectory
    for _ in range(1000):
        new_x = current_pos[0] + current_trajectory[0]
        new_y = current_pos[1] + current_trajectory[1]
        current_pos = (new_x, new_y)

        new_t_x = (
            current_trajectory[0] - 1
            if current_trajectory[0] > 0
            else current_trajectory[0]
        )
        new_t_y = current_trajectory[1] - 1
        current_trajectory = (new_t_x, new_t_y)

        if new_x in target[0] and new_y in target[1]:
            # inside
            return True

        if new_y < target[1][0]:
            # outwith bounds
            return False

    # give up
    return False


def find_possible_trajectories(target):
    highest_possible_x = range(target[0][-1] + 1)
    lowest_possible_y = target[1][0]
    highest_possible_y = 150  # guess, could be clever with x, but cpu can handle it!

    possible = []
    for px in highest_possible_x:
        for py in range(lowest_possible_y, highest_possible_y):
            if passes_through_target((px, py), target):
                possible.append((px, py))
    return possible


def part_one(target):
    possible = find_possible_trajectories(target)
    highest_y = sorted(possible, key=lambda x: x[1], reverse=True)
    return triangular_number(highest_y[0][1])


def part_two(target):
    possible = find_possible_trajectories(target)
    return len(possible)


advent_of_code(
    {
        "day": 17,
        "part": 1,
        "fn": part_one,
        "sample": (range(20, 30), range(-10, -5 + 1)),
        "expected": 45,
        "real": (range(211, 232), range(-124, -69 + 1)),
        # 7626
    }
)

advent_of_code(
    {
        "day": 17,
        "part": 2,
        "fn": part_two,
        "sample": (range(20, 30 + 1), range(-10, -5 + 1)),
        "expected": 112,
        "real": (range(211, 232 + 1), range(-124, -69 + 1)),
        # 2032
    }
)
