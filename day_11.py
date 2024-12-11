def d11_blink(stones: list, blinks) -> list:
    def blink(s, depth=0):
        key = (s, depth)
        if depth >= blinks: return 1
        if key in values:
            return values[key]
        if s == 0:
            score = blink(1, depth+1)
        elif not len(str(s)) % 2 and s>9:
            s = str(s)
            s1 = int(s[:len(s)//2])
            s2 = int(s[len(s)//2:])
            score = blink(s1, depth+1) + blink(s2, depth+1)
        else: 
            score = blink(s*2024, depth+1)
        values[key] = score
        return score
    total_score = 0
    values = {}
    for s in stones:
        total_score += blink(s)
    return total_score

def day11_solve(input: str, blinks: int = 25) -> int:
    stones = list(map(int, input.strip("\n").split(" ")))
    return d11_blink(stones, blinks)
