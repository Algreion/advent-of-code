# https://adventofcode.com/2024/day/2

def d2_parse(string):
    x = string.split("\n")
    for i in range(len(x)):
        x[i] = x[i].split()
        for j,n in enumerate(x[i]):
            x[i][j] = int(n)
    return x

def day2_solve1(input: str, split=True) -> int: # Ans: 279
    if split: input = d2_parse(input)
    n = 0
    for report in input:
        safe, i, increase = 1, 0, 0
        while i < len(report)-1 and safe:
            v = report[i]
            if i == 0:
                if report[i+1] == v:
                    safe = 0
                    break
                elif report[i+1] > v:
                    increase = 1
            if increase:
                if report[i+1] <= v or report[i+1]-3 > v: safe = 0
            else:
                if report[i+1] >= v or report[i+1]+3 < v: safe = 0
            i += 1
        n += safe
    return n

def day2_solve2(input: str) -> int: # Ans: 343
    n = 0
    input = d2_parse(input)
    for report in input:
        if day2_solve1([report], False):
            n += 1
            continue
        for i in range(len(report)):
            if day2_solve1([report[:i]+report[i+1:]], False):
                n += 1
                break
    return n
