import input_12
from aoc import advent_of_code
from collections import defaultdict, Counter


def discover_world(input):
    routes = defaultdict(list)
    small_caves = set()

    for start, end in input:
        routes[start].append(end)

        if start != "START":
            routes[end].append(start)

        if start.islower():
            small_caves.add(start)
        if end.islower():
            small_caves.add(end)

    return (routes, small_caves)


fin = []


def visit(current, visited, routes, small_caves):
    if current == "END":
        fin.append(visited)
        return

    for possible in routes[current]:
        if possible in small_caves and possible in visited:
            continue

        new_visited = visited.copy()
        new_visited.append(possible)
        visit(possible, new_visited, routes, small_caves)


def part_one(input):
    fin.clear()
    routes, small_caves = discover_world(input)
    visit("START", ["START"], routes, small_caves)
    return len(fin)


def visit2(current, visited, routes, small_caves):
    if current == "END":
        fin.append(visited)
        return

    visited_small_caves = filter(lambda x: x in small_caves, visited)
    most_common = Counter(visited_small_caves).most_common(1)
    visited_small_cave_twice_already = len(most_common) == 1 and most_common[0][1] == 2

    for possible in routes[current]:
        if (
            visited_small_cave_twice_already
            and possible in small_caves
            and possible in visited
        ):
            continue

        new_visited = visited.copy()
        new_visited.append(possible)
        visit2(possible, new_visited, routes, small_caves)


def part_two(input):
    fin.clear()
    routes, small_caves = discover_world(input)
    visit2("START", ["START"], routes, small_caves)
    return len(fin)


advent_of_code(
    {
        "day": 12,
        "part": 1,
        "fn": part_one,
        "sample": input_12.sample(),
        "expected": 10,
        "real": input_12.real(),
    }
)

advent_of_code(
    {
        "day": 12,
        "part": 2,
        "fn": part_two,
        "sample": input_12.sample(),
        "expected": 36,
        "real": input_12.real(),
    }
)
