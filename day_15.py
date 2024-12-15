
def d15_push(map: list, r: int, c: int, dr: int, dc: int) -> list:
    if not (0<=r<len(map)) or not (0<=c<len(map[0])) or map[r][c] in "#.": return []
    char, map[r][c] = map[r][c], "."
    comp = [(r, c, char)]
    comp.extend(d15_push(map, r+dr, c+dc, dr, dc))
    if char == "[": comp.extend(d15_push(map, r, c+1, dr, dc))
    if char == "]": comp.extend(d15_push(map, r, c-1, dr, dc))
    return comp

def d15_p2(ch):
  if ch == "@": return ["@", "."]
  elif ch == ".": return [".", "."]
  elif ch == "#": return ["#", "#"]
  else: return ["[", "]"]

def d15_solver(grid: list, moves: str) -> int:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@": r, c = i,j
    for move in moves:
        if move == "v": dr, dc = 1, 0
        elif move == "^": dr, dc = -1, 0
        elif move == ">": dr, dc = 0, 1
        elif move == "<": dr, dc = 0, -1
        else: continue
        comp = d15_push(grid, r, c, dr, dc)
        if all(grid[i+dr][j+dc] == "." for i, j, _ in comp):
            comp = [(i+dr, j+dc, ch) for i, j, ch in comp]
            r, c = r+dr, c+dc
        for rr, cc, char in comp:
            grid[rr][cc] = char
    return sum(sum(i*100 + j for j,ch in enumerate(line) if ch in "O[") for i, line in enumerate(grid))

def day15_solve(input: str) -> None: # Ans1: 1371036 | Ans2: 1392847
    map, moves = input.split("\n\n")
    map1 = [list(line) for line in map.split("\n")]
    map2 = [sum((d15_p2(c) for c in line), []) for line in map.split("\n")]
    print(f"Part 1 solution: {d15_solver(map1, moves)}")
    print(f"Part 2 solution: {d15_solver(map2, moves)}")

