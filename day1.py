# https://adventofcode.com/2024/day/1

def d1_distance_solve(arr):
    arr1, arr2 = arr
    diff = 0
    res = zip(sorted(arr1),sorted(arr2))
    for i in res:
        diff += abs(i[0]-i[1])
    return diff

def d1_parse(string):
    arr1 = []
    arr2 = []
    for i,n in enumerate(string.split()):
        if not i%2: arr1.append(int(n))
        else: arr2.append(int(n))
    return [arr1,arr2]

def day1_solve1(input: str) -> int: # Ans: 3714264
    return d1_distance_solve(d1_parse(input))

def day1_solve2(input: str) -> int: # Ans: 18805872
    n = 0
    arr1, arr2 = d1_parse(input)
    hist = {}
    for v in arr2:
        hist[v] = hist.get(v, 0) + 1
    for v in arr1:
        n += v*hist.get(v,0)
    return n
