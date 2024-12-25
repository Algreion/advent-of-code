def d25_parse(input: str) -> tuple:
    keys, locks = dict(), dict()
    h = -1
    for item in input.split("\n\n"):
        lock = False
        heights = dict()
        for i,line in enumerate(item.splitlines()):
            if h == -1: h = len(item.splitlines())
            if i == 0 and "#" in line: lock = True
            if lock:
                for j in range(len(line)):
                    if line[j] != "#" and j not in heights: heights[j] = i-1
            else:
                for j in range(len(line)):
                    if line[j] == "#" and j not in heights: heights[j] = h-1-i
        heights = tuple(v for _,v in sorted(heights.items()))
        if lock: locks[heights] = locks.get(heights, 0) + 1
        else: keys[heights] = keys.get(heights, 0) + 1
    return (keys, locks, h)

def day25_solve(input: str) -> int: # Ans: 3663
    keys, locks, h = d25_parse(input)
    matches = 0
    for k in keys:
        for l in locks:
            yep = True
            for i in range(len(k)):
                if k[i] + l[i] >= h-1: yep = False
            if yep: 
                matches += keys[k] * locks[l]
    return matches
