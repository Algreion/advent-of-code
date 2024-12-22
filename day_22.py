
def d22_pr(n: int) -> int:
    n ^= n<<6
    n %= 1<<24
    n ^= n>>5
    n %= 1<<24
    n ^= n<<11
    n %= 1<<24
    return n

def d22_run(n: int) -> int:
    for _ in range(2000):
        n = d22_pr(n)
    return n

def day22_solve(input: str) -> int: # Ans: 13429191512
    return sum(d22_run(int(n)) for n in input.splitlines())


