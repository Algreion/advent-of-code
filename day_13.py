# Solution using Z3 | https://adventofcode.com/2024/day/13

from collections import defaultdict

def d13_parse(input: str) -> dict:
    res = defaultdict(list)
    i = 0
    for line in input.splitlines():
        if not line: 
            i += 1
            continue
        line = line.replace("+"," ").replace(","," ").replace("="," ")
        for n in line.split():
            if n.isdigit(): res[i].append(int(n))
    return res

def d13_z3_a(n: list, file: str = "day_13-1.txt") -> None:
    """Writes the assertion for one claw machine"""
    with open(file,"a") as f:
        i,ax,ay,bx,by,x,y = n[-1],n[0],n[1],n[2],n[3],n[4],n[5]
        f.write(
f"""
(push)
(declare-const Tokens{i} Int)
(declare-const A{i} Int)
(declare-const B{i} Int)
(declare-const x{i} Int)
(declare-const y{i} Int)

(assert (and (= x{i} {x}) (= y{i} {y})))
(assert (= Tokens{i} (+ B{i} (* 3 A{i}))))
(assert (= x{i} (+ (* B{i} {bx}) (* A{i} {ax}))))
(assert (= y{i} (+ (* B{i} {by}) (* A{i} {ay}))))

(minimize Tokens{i})
(check-sat)
(get-value (Tokens{i}))
(pop)
\n""")

def d13_z3_b(n: list, file: str = "day_13-2.txt") -> None:
    """Writes the assertion for one claw machine"""
    with open(file,"a") as f:
        i,ax,ay,bx,by,x,y = n[-1],n[0],n[1],n[2],n[3],n[4],n[5]
        f.write(
    f"""
(push)
(declare-const Tokens{i} Int)
(declare-const A{i} Int)
(declare-const B{i} Int)
(declare-const x{i} Int)
(declare-const y{i} Int)

(assert (and (= x{i} {x+10000000000000}) (= y{i} {y+10000000000000})))
(assert (= Tokens{i} (+ B{i} (* 3 A{i}))))
(assert (= x{i} (+ (* B{i} {bx}) (* A{i} {ax}))))
(assert (= y{i} (+ (* B{i} {by}) (* A{i} {ay}))))

(minimize Tokens{i})
(check-sat)
(get-value (Tokens{i}))
(pop)
    \n""")

def d13_write(input: str) -> bool:
    """Writes the full Z3 file"""
    nums = d13_parse(input)
    for i in nums:
        nums[i].append(i)
        d13_z3_a(nums[i])
        d13_z3_b(nums[i])
    return True

def d13_solve(result: str) -> int:
    """Reads the result from Z3"""
    tokens = 0
    for line in result.splitlines():
        if len(line) > 33: continue
        for n in line.strip("))").split():
            if n.isdigit(): tokens += int(n)
    return tokens

# Instructions: 
# 1. Run d13_write(input) for the raw puzzle input.
# 2. Run the day_13-1.txt and day_13-2.txt files with Z3
# 3. Copy paste the entire result of one of the two parts in d13_solve(result)

# Answer 1: 37680
# Answer 2: 87550094242995

