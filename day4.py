# https://adventofcode.com/2024/day/4

def d4_parse(string):
    res, add = [], []
    for c in string:
        if c == "\n":
            res.append(add[:])
            add.clear()
        else: add.append(c)
    res.append(add)
    return res

def day4_solve1(input: str) -> int: # Ans: 2414
    input = d4_parse(input)
    n = 0
    def find(i, j):
        nonlocal n
        start_i, start_j = i, j
        path = "X"
        dirs = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        for dr, dc in dirs:
            for _ in range(3):
                i += dr
                j += dc
                path += input[r][c]
            if path == "XMAS": n += 1
            path, i, j = "X", start_i, start_j

    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] == "X": find(r, c)
    return n

def day4_solve2(input: str) -> int: # Ans: 1871
    input = d4_parse(input)
    n = 0
    matches = {"M":"S","S":"M"}
    def find_x(i, j):
        nonlocal n
        if (i+1 >= len(input) or j+1 >= len(input[0]) or i==0 or j==0): return
        check = (input[i+1][j+1],input[i-1][j-1],input[i+1][j-1],input[i-1][j+1])
        if (any(c not in matches for c in check) 
            or matches[check[0]] != check[1]
            or matches[check[2]] != check[3]): return
        n += 1
    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] == "A": find_x(r, c)
    return n