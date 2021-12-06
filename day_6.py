import input_6
from aoc import advent_of_code


def day_cycle(fish):
    if fish == 0:
        return 6
    return fish - 1


def part_one(input):
    for _ in range(80):
        zeros = len(list(filter(lambda x: x == 0, input)))
        input = list(map(day_cycle, input))
        input += [8] * zeros

    return len(input)


def part_two(input):
    fish_by_days = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    for fish in input:
        fish_by_days[fish] += 1

    for _ in range(0, 256):
        zeros = fish_by_days[0]

        fish_by_days[0] = fish_by_days[1]
        fish_by_days[1] = fish_by_days[2]
        fish_by_days[2] = fish_by_days[3]
        fish_by_days[3] = fish_by_days[4]
        fish_by_days[4] = fish_by_days[5]
        fish_by_days[5] = fish_by_days[6]
        fish_by_days[6] = fish_by_days[7] + zeros
        fish_by_days[7] = fish_by_days[8]
        fish_by_days[8] = zeros

    return sum(fish_by_days.values())


advent_of_code(
    {
        "day": 6,
        "part": 1,
        "fn": part_one,
        "sample": input_6.sample(),
        "expected": 5934,
        "real": input_6.real(),
    }
)

advent_of_code(
    {
        "day": 6,
        "part": 2,
        "fn": part_two,
        "sample": input_6.sample(),
        "expected": 26984457539,
        "real": input_6.real(),
    }
)
