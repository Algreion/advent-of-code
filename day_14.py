# https://adventofcode.com/2024/day/14

BX, BY = 101, 103
SECONDS = 10
ANS = 7093

def d14_parse(input: str) -> list:
    res = []
    for line in input.splitlines():
        if not line: continue
        robot = []
        line = line.replace("="," ").replace(","," ")
        for c in line.split():
            if c.isdigit() or c.startswith("-"): robot.append(int(c))
        res.append(robot)
    return res

def d14_move(robot: list, time: int = SECONDS) -> tuple:
    x, y, vx, vy = robot
    bx, by = BX, BY
    while time > 0:
        x += vx
        y += vy
        while x >= bx: x -= bx
        while y >= by: y -= by
        while x < 0: x += bx
        while y < 0: y += by
        time -= 1
    if not (0<=x<bx) or not (0<=y<by): print(x,y, robot)
    return (x, y)

def d14_quadrants(grid: list) -> int:
    by, bx = len(grid), len(grid[0])
    q1,q2,q3,q4 = 0, 0, 0, 0
    for y in range(by):
        for x in range(bx):
            n = grid[y][x]
            if n==0: continue
            if y < by//2 and x < bx//2: q1 += n
            elif y < by//2 and x > bx//2: q2 += n
            elif y > by//2 and x < bx//2: q3 += n
            elif y > by//2 and x > bx//2: q4 += n
    return q1*q2*q3*q4

def day14_solve1 (input: str) -> int: # Ans: 228690000
    grid = [[0 for _ in range(BX)] for _ in range(BY)]
    robots = d14_parse(input)
    for r in robots:
        x,y = d14_move(r)
        grid[y][x] += 1
    return d14_quadrants(grid)

def d14_surely_there_is_a_faster_method(input: str, r: tuple) -> None:
    i, j = r
    for sec in range(i,j):
        print(sec)
        day14_solve2(input, sec)

def day14_solve2 (input: str, s: int = ANS, res=False) -> None: # Ans: 7093
    robots = d14_parse(input)
    grid = [[" " for _ in range(BX)] for _ in range(BY)]
    for r in robots:
        x,y = d14_move(r, s)
        grid[y][x] = "X"
    if not res: print(grid)
    else: return grid
    
def day14_visualizer(input: str) -> bool: # Cool tree I guess...
    grid = day14_solve2(input, res=True)
    with open("day_14-tree.txt","w") as f:
        for line in grid:
            f.write("".join(line))
            f.write("\n")
    return True

    