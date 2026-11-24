# https://adventofcode.com/2024/day/5

def d5_parse(input: str) -> dict:
    # Parsing instructions
    input = input.split("\n")
    for i in range(len(input)):
        input[i] = input[i].split("|")
        input[i][0], input[i][1] = int(input[i][0]), int(input[i][1])
    # Initializing dictionary
    nodes = {}
    for pair in input:
        if pair[0] not in nodes:
            nodes[pair[0]] = set()
        if pair[1] not in nodes:
            nodes[pair[1]] = set()
        nodes[pair[0]].add(pair[1])
    return nodes
def d5_parse_input(input: str) -> list:
    input = input.split("\n")
    for i in range(len(input)):
        input[i] = input[i].split(",")
        for j in range(len(input[i])): input[i][j] = int(input[i][j])
    return input
def d5_check(nodes: dict, pages: list) -> bool:
        seen = set()
        for v in pages:
            for n in nodes.get(v, set()):
                if n in seen: return False
            seen.add(v)
        return True
def d5_reorder(dependencies: dict, pages: list):
    if d5_check(dependencies, pages): return False
    # Doubly linked graph of dependencies
    positions = {}
    for key, after in dependencies.items():
        if key not in positions:
            positions[key] = {"after": set(), "before": set()}
        positions[key]["after"].update(after)

        for after_i in after:
            if after_i not in positions:
                positions[after_i] = {"after": set(), "before": set()}
            positions[after_i]["before"].add(key)
    
    # Topological sorting
    def find_min_index(item, path):
        if item not in positions:
            return len(path)
        
        after_min_index = 0
        for after_i in positions[item].get("after", set()):
            if after_i in path:
                after_min_index = max(after_min_index, path.index(after_i) + 1)
        
        before_max_index = len(path)
        for before_i in positions[item].get("before", set()):
            if before_i in path:
                before_max_index = min(before_max_index, path.index(before_i))

        return min(after_min_index, before_max_index)
    
    sorted_list = []
    remaining = set(pages)
    
    while remaining:
        for item in list(remaining):
            index = find_min_index(item, sorted_list)

            sorted_list.insert(index, item)
            remaining.remove(item)
            break
    
    return sorted_list[::-1]

def day5_solve1(instructions: str, input: str) -> int: # Ans: 4662
    nodes = d5_parse(instructions)
    input = d5_parse_input(input)
    # Solve
    res = 0
    for pages in input:
        if d5_check(nodes, pages):
            res += pages[len(pages)//2]
    return res

def day5_solve2(instructions: str, input: str) -> int: # Ans: 5900
    nodes = d5_parse(instructions)
    input = d5_parse_input(input)
    res = 0
    for pages in input:
        pages = d5_reorder(nodes, pages)
        if pages:
            res += pages[len(pages)//2]
    return res
