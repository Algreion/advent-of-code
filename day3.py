# https://adventofcode.com/2024/day/3

def day3_solve1(input: str, do=False) -> int: # Ans: 181345830
    ruleset = {"m":"u","u":"l","l":"("}
    i, n = 0, 0
    path = ""
    on = True
    while i < len(input):
        c = input[i]
        if on and path:
            if (path[-1] in ruleset and ruleset[path[-1]] == c) or (path[-1] == "(" and c.isdigit()) or (path[-1] == "," and c.isdigit()):
                path += c
            elif path[-1].isdigit():
                if "," in path and (c == ")" or c.isdigit()):
                    path += c
                elif "," not in path and (c.isdigit() or c == ","):
                    path += c
                else: path = ""
            else:
                path = ""
        elif on and c == "m": path += c
        if on and path and path[-1] == ")":
            path = path.strip("mul()").split(",")
            n += int(path[0])*int(path[1])
            path = ""
        if do and c == "d":
            on = True if input[i:i+4] == "do()" else False if input[i:i+7] == "don't()" else on
        i += 1
    return n

def day3_solve2(input: str) -> int: # Ans: 98729041
    return day3_solve1(input, True)
