def d24_solver(input: str, fin: str = "day_24.clj") -> None:
    with open(fin, "w") as f:
        in1, in2 = input.split("\n\n")
        const = set()
        for line in in1.splitlines():
            x,y = line.split(": ")
            const.add(x)
            f.write(f"(declare-const {x} Bool)\n(assert (= {x} {"true" if int(y) else "false"}))\n")
        for line in in2.splitlines():
            a, b, c, d = line.replace("-> ","").split()
            for x in [a,c,d]:
                if x not in const: 
                    f.write(f"\n(declare-const {x} Bool)")
                    const.add(x)
            f.write(f"\n(assert (= ({b.lower()} {a} {c}) {d}))")
        f.write("\n(check-sat)\n(get-value (")
        for x in sorted(const, reverse=True):
            if x[0] == "z":
                f.write(f"{x} ")
            else:
                f.write("))")
                break

def day24_solve(result: str) -> int: # Ans: 49430469426918
    res = ""
    for line in result.splitlines():
        if "true" in line: res += "1"
        elif "false" in line: res += "0"
    return int(res, 2)

