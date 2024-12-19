from functools import cache

@cache
def d19_check(pattern: str, towels: list) -> int:
    n = 0
    for t in towels:
        if pattern == t: n += 1
        if pattern.startswith(t): n += d19_check(pattern.removeprefix(t), towels)
    return n

def day19_solve(input: str) -> None: # Ans1: 302 | Ans2: 771745460576799
    total1 = 0
    total2 = 0
    towels, patterns = input.splitlines()[0], input.splitlines()[1:]
    towels = tuple(sorted([t for t in towels.split(", ")], key=len, reverse=True))
    for p in patterns:
        x = d19_check(p, towels)
        total2 += x
        total1 += (x != 0)
    print(f"Part 1 | Number of possible designs: {total1}")
    print(f"Part 2 | Number of unique designs: {total2}")
