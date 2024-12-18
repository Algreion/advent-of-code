import heapq

D18_ROWS, D18_COLS = 71, 71

def d18_parse(input: str, ns: int = 1024) -> list:
    corrupt = [tuple(map(int,line.split(","))) for line in input.splitlines()[:ns]]
    grid = [["." for _ in range(D18_COLS)] for _ in range(D18_ROWS)]
    for x,y in corrupt:
        grid[x][y] = "#"
    return grid

def d18_distance(x,y):
    xe,ye = D18_COLS-1, D18_COLS-1
    return abs(x-xe) + abs(y-ye) # (Manhattan Distance)

def d18_pathfind(grid: list) -> int:
    start, end = (0,0), (D18_COLS-1, D18_COLS-1)
    check = [(0, *start, 0)]
    processed = set()
    dirs = [(0,1),(1,0),(-1,0),(0,-1)]
    best = {start: 0}
    while check:
        _, x, y, s = heapq.heappop(check)
        if (x,y) == end: return s
        if (x,y) in processed: continue
        processed.add((x,y))
        for dr,dc in dirs:
            r,c = x+dr,y+dc
            if not (0 <= r < D18_ROWS) or not (0 <= c < D18_COLS) or grid[r][c] == "#" or (r,c) in processed: continue
            score = s+1
            if (r,c) not in best or score < best[(r,c)]:
                best[(r,c)] = score
                dist = score + d18_distance(r,c)
                heapq.heappush(check, (dist, r, c, score))
    return -1


def day18_solve1(input: str) -> int: # Ans: 354
    return d18_pathfind(d18_parse(input))

def day18_solve2(input: str, loading: bool = True) -> int: # Ans: 36,17
    for ns in range(1024, len(input.splitlines())):
        if not ns % 100 and loading: print(ns)
        if d18_pathfind(d18_parse(input, ns)) == -1: return input.splitlines()[ns-1] # ns-1 because 0-indexed
