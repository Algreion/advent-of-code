# https://adventofcode.com/2024/day/12

def d12_parse(input: str) -> list:
    return [list(line) for line in input.splitlines()]

def d12_convert(grid: list) -> list:
    areas = set()
    done = set()
    rows, cols = len(grid), len(grid[0])

    def convert(r, c):
        nonlocal done, grid
        area = set()
        letter = grid[r][c]
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(i, j):
            nonlocal area
            if not (0 <= i < rows) or not (0 <= j < cols) or grid[i][j] != letter or (i,j) in area: return
            area.add((i, j))
            for dr,dc in dirs: 
                dfs(i+dr,j+dc)

        dfs(r,c)
        while letter in areas:
            letter = chr(ord(letter)+1)
        
        for x,y in area:
            grid[x][y] = letter
            done.add((x,y))
    
    for r in range(rows):
        for c in range(cols):
            if (r,c) not in done: convert(r, c)
            areas.add(grid[r][c])
    return grid

def d12_count_corners(grid, i, j):

    def get_area(grid, i, j, c):
        area = set()
        check = [(i, j)]
        while check:
            x, y = check.pop()
            if (x, y) not in area and 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == c:
                area.add((x, y))
                check.extend([(x-1, y), (x+1, y), (x, y-1), (x, y+1)])
        return area

    def find_corners(area):
        corners, double = set(), 0
        xs, ys = set(x for x, _ in area), set(y for _, y in area) # Unique x, y | Boundary is min(x/y), max(x/y)
        for y in range(min(ys), max(ys) + 2):
            for x in range(min(xs), max(xs) + 2): # Expand boundary by 1
                index = sum(((x + dx, y + dy) in area) * val
                            for dx, dy, val in [(-1, -1, 1), (-1, 0, 2), (0, -1, 4), (0, 0, 8)])
                if index not in [0, 3, 5, 10, 12, 15]: # Corners are all except these
                    corners.add((x, y))
                if index in [6, 9]:
                    double += 1
        return len(corners) + double

    area = get_area(grid, i, j, grid[i][j])
    return find_corners(area)


def day12_solve(input: str, part2=False) -> int: # Ans1: 1518548 | Ans2: 909564
    grid = d12_convert(d12_parse(input))
    a, p = {}, {}
    dirs = [(0,1),(1,0),(-1,0),(0,-1)]
    rows, cols = len(grid), len(grid[0])
    done = set()
    for r in range(rows):
        for c in range(cols):
            letter = grid[r][c]
            a[letter] = a.get(letter, 0) + 1

            if part2 and letter not in done: # Part 2 perimeter counting
                p[letter] = d12_count_corners(grid, r, c)
                done.add(letter)
            
            for dr, dc in dirs:
                if not (0 <= r+dr < rows) or not (0 <= c+dc < cols) or grid[r+dr][c+dc] != letter:
                    if not part2: p[letter] = p.get(letter, 0) + 1 # Part 1 perimeter counting
    res = 0
    for k in a:
        res += a[k] * p[k]
    return res
