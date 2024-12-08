from collections import defaultdict
from itertools import combinations

def d8_parse(input: str) -> list:
    return [list(row) for row in input.split("\n")]

def d8_antinodes1(grid: list, antennas: dict) -> int:
    antinodes = set()
    rows, cols = len(grid), len(grid[0])
    for key in antennas:
        for (r1, c1),(r2,c2) in combinations(antennas[key],2):
            dr, dc = r2 - r1, c2-c1
            if 0 <= r1-dr < rows and 0 <= c1-dc < cols: antinodes.add((r1-dr, c1-dc))
            if 0 <= r2+dr < rows and 0 <= c2+dc < cols: antinodes.add((r2+dr, c2+dc))
    return len(antinodes)

def d8_antinodes2(grid: list, antennas: dict) -> int:
    antinodes = set()
    rows, cols = len(grid), len(grid[0])
    for key in antennas:
        for (r1, c1),(r2, c2) in combinations(antennas[key],2):
            dr, dc = r1-r2, c1-c2
            for i in range(cols):
                ax, ay = r1 + i*dr, c1 + i*dc
                bx, by = r2 - i*dr, c2 - i*dc
                if 0 <= ax < rows and 0 <= ay < cols: antinodes.add((ax, ay))
                if 0 <= bx < rows and 0 <= by < cols: antinodes.add((bx, by))
    return len(antinodes)


def day8_solve(input: str, part2=False) -> int: # Ans1: 426 | Ans2: 1359
    grid = d8_parse(input)
    frequencies = defaultdict(set)
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != ".": frequencies[grid[r][c]].add((r,c))
    if part2: return d8_antinodes2(grid, frequencies)
    return d8_antinodes1(grid, frequencies)

