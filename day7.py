# https://adventofcode.com/2024/day/7

def d7_parse(input: str) -> list:
    return [list(map(int, line.replace(":","").split()))
            for line in input.splitlines()]
            
def d7_check(target: int, vals: list, i: int=0, path: int=0, two=False) -> bool:
    if i == 0:
        return d7_check(target, vals, 1, vals[0], two)
    else:
        if i >= len(vals):
            return True if target == path else False
        if two:
            return (d7_check(target, vals, i+1, path+vals[i], True) or d7_check(target, vals, i+1, path*vals[i], True)
                    or d7_check(target, vals, i+1, int(str(path)+str(vals[i])), True))
        return d7_check(target, vals, i+1, path+vals[i]) or d7_check(target, vals, i+1, path*vals[i])

def day7_solve(input: str, part2=False) -> int: # Ans1: 1399219271639 | Ans2: 275791737999003
    input = d7_parse(input)
    res = 0
    for item in input:
        if d7_check(item[0], item[1:], two=part2): res += item[0]
    return res
  
