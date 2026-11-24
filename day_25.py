def d25_parse(input: str) -> tuple:
    keys, locks = {}, {}
    input = [item.splitlines() for item in input.split("\n\n")]
    h = len(input[0])-1
    for item in input:
        lock = "#" in item[0]
        heights = {}
        for i,line in enumerate(item):
            for j, c in enumerate(line):
                if lock and c != "#" and j not in heights: heights[j] = i-1
                elif not lock and c == "#" and j not in heights: heights[j] = h-i
        heights = tuple(v for _,v in sorted(heights.items()))
        group = locks if lock else keys
        group[heights] = group.get(heights, 0) + 1
    return (keys, locks, h)

def day25_solve(input: str) -> int: # Ans: 3663
    keys, locks, h = d25_parse(input)
    matches = 0
    for k, k_i in keys.items():
        for l, l_i in locks.items():
            if all(k[i] + l[i] < h for i in range(len(k))): matches += k_i * l_i
    return matches
