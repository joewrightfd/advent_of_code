from aoc import advent_of_code


def triangular_number(n):
    return int(n * (n + 1) / 2)


def passes_through_target(trajectory, target):
    current_pos = (0, 0)
    current_trajectory = trajectory
    for step in range(1000):
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
            # print(trajectory, "inside at", current_pos, "after", step)
            return True

        if new_y < target[1][0]:
            # print(
            #     trajectory, "overshot at", current_pos, "which is outwith", target[1][0]
            # )
            return False

    # print("given up at", current_pos, "after 100 rounds")
    return False


def part_one(target):
    print("=" * 80)

    possbile_x = []
    for n in range(1000):
        if triangular_number(n) in target[0]:
            possbile_x.append(n)

    print("pos x", possbile_x)

    possible = []
    for px in possbile_x:
        for py in range(1000):
            if passes_through_target((px, py), target):
                possible.append((px, py))

    highest_y = sorted(possible, key=lambda x: x[1], reverse=True)
    print("pos y", possible)

    return triangular_number(highest_y[0][1])


advent_of_code(
    {
        "day": 17,
        "part": 1,
        "fn": part_one,
        "sample": (range(20, 30), range(-10, -5)),
        "expected": 45,
        "real": (range(211, 232), range(-124, -69)),
    }
)
