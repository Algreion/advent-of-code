import heapq

def d16_parse(input: str) -> tuple:
    maze = [list(line) for line in input.splitlines()]
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == "S": start = (r,c)
            if maze[r][c] == "E": end = (r,c)
    return (maze,start,end)

def d16_pathfind(grid: list, start: tuple, end: tuple) -> int:
    check = [(0, *start, (0, 0))]
    processed = set()
    dirs = [(0,1),(1,0),(-1,0),(0,-1)]
    rows, cols = len(grid), len(grid[0])
    while check:
        s, x, y, d = heapq.heappop(check)
        if (x,y) == end: return s
        processed.add((x,y))
        for dr,dc in dirs:
            r,c = x+dr,y+dc
            if not (0<=r<rows) or not (0<=c<cols) or grid[r][c] == "#": continue
            elif (r,c) not in processed:
                score = s+1 if (dr,dc) == d else s+1001
                heapq.heappush(check, (score, r,c, (dr, dc)))
    return False

def day16_solve(input: str) -> int: # Ans: 66404
    info = d16_parse(input)
    return d16_pathfind(*info)
