# https://adventofcode.com/2024/day/10

def d10_find_paths(grid: list, r: int, c: int, p2=False) -> int:
    dirs = [(0,1),(1,0),(-1,0),(0,-1)]
    seen = set()
    def search(i: int, j: int, path: int, paths=0):
        if not (0<=i<len(grid)) or not (0<=j<len(grid[0])) or grid[i][j] != path: return 0
        if path == 9:
            if p2: return 1
            if (i,j) in seen: return 0
            seen.add((i,j))
            return 1
        for dr, dc in dirs:
            paths += search(i+dr, j+dc, path+1)
        return paths
    return search(r, c, 0)

def d10_parse(input: str) -> list:
    return [list(map(int, list(line))) for line in input.splitlines()]

def day10_solve(input: str, part2=False) -> int: # Ans1: 531 | Ans2: 1210
    grid = d10_parse(input)
    paths = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0: paths += d10_find_paths(grid, r, c, part2)
    return paths
  
