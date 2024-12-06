# https://adventofcode.com/2024/day/6

def d6_parse(input: str) -> list:
    input = input.split("\n")
    for i in range(len(input)):
        input[i] = list(input[i])
    return input

def day6_solve1(input: str) -> int: # Ans: 5153
    grid = d6_parse(input)
    rows, cols = len(grid),len(grid[0])
    guard = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in "<v^>": 
                guard = (r,c)
                break
        if guard: break
    directions = {"^":((-1,0),">"),"v":((1,0),"<"),"<":((0,-1),"^"),">":((0,1),"v")}
    i,j = guard
    while 0<=i<rows and 0<=j<cols:
        guard = grid[i][j]
        dr,dc = directions[guard][0]
        if 0<=i+dr<rows and 0<=j+dc<cols:
            if grid[i+dr][j+dc] == "#":
                grid[i][j] = directions[guard][1]
                continue
            grid[i+dr][j+dc] = guard
        grid[i][j] = "X"
        i += dr
        j += dc
    path = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "X": path += 1
    return path

def d6_move(grid, start, rows, cols):
    directions = {"^": ((-1, 0), ">"), "v": ((1, 0), "<"), "<": ((0, -1), "^"), ">": ((0, 1), "v")}
    visited = set()
    i, j, direction = start

    while 0 <= i < rows and 0 <= j < cols:
        cell = (i, j, direction)
        if cell in visited: return True # Loop check
        visited.add(cell)

        dr, dc = directions[direction][0]
        if 0 <= i + dr < rows and 0 <= j + dc < cols and grid[i + dr][j + dc] == "#":
            direction = directions[direction][1]
        else:
            i += dr
            j += dc

    return False 

def day6_solve2(input: str, load=True) -> int: # Ans: 1711
    grid = d6_parse(input)
    rows, cols = len(grid), len(grid[0])
    start = None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in "<v^>":
                start = (r, c, grid[r][c])
                grid[r][c] = "."
                break

    paradox = 0

    for r in range(rows):
        for c in range(cols):
            if load: print(r,c)
            if grid[r][c] == ".":
                grid[r][c] = "#"
                if d6_move(grid, start, rows, cols):
                    paradox += 1
                grid[r][c] = "." # Backtrack

    return paradox

