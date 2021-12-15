import input_15
from aoc import advent_of_code

import sys
import heapq


class Solver:
    def __init__(self, grid):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])

    def neighbouring_cells(self, x, y, scale):
        neighbours = [
            (x, y + 1),
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
        ]

        def in_bounds(cord):
            x, y = cord
            return (
                y >= 0 and x >= 0 and y < self.height * scale and x < self.width * scale
            )

        return filter(in_bounds, neighbours)

    def scaled_cost(self, x, y, scale):
        if scale == 1:
            return self.grid[y][x]

        base_cost = self.grid[y % self.height][x % self.width]
        scale_cost = int(x / self.width) + int(y / self.height) - 1
        return (base_cost + scale_cost) % 9 + 1

    def dijkstra(self, start, scale):
        # https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/
        distances = {start: 0}

        pqueue = [(start, 0)]
        while pqueue:
            (x, y), total = heapq.heappop(pqueue)

            if total <= distances[(x, y)]:
                for (nx, ny) in self.neighbouring_cells(x, y, scale):
                    distance = total + self.scaled_cost(nx, ny, scale)
                    if distance < distances.get((nx, ny), sys.maxsize):
                        distances[(nx, ny)] = distance
                        heapq.heappush(pqueue, ((nx, ny), distance))

        end = ((self.width * scale) - 1, (self.height * scale) - 1)
        return distances[end]


def part_one(grid):
    return Solver(grid).dijkstra((0, 0), 1)


def part_two(grid):
    return Solver(grid).dijkstra((0, 0), 5)


advent_of_code(
    {
        "day": 15,
        "part": 1,
        "fn": part_one,
        "sample": input_15.sample(),
        "expected": 40,
        "real": input_15.real(),  #  589
    }
)

advent_of_code(
    {
        "day": 15,
        "part": 2,
        "fn": part_two,
        "sample": input_15.sample(),
        "expected": 315,
        "real": input_15.real(),
    }
)
