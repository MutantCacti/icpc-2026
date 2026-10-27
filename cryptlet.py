
def to_number(st, abcde):
    lst = list(st)
    for i,char in enumerate(lst):
        lst[i] = str(abcde[char])
    return int("".join(lst))


def try_all_recursive(lop, rop, rhs, abcde, remaining):
    if len(remaining) == 0:
        nlop = to_number(lop, abcde)
        nrop = to_number(rop, abcde)
        nrhs = to_number(rhs, abcde)
        if nlop + nrop == nrhs:
            print(f"{abcde['a']}{abcde['b']}{abcde['c']}{abcde['d']}{abcde['e']}")
            exit(0)
    character = remaining.pop(0)
    for i in range(10):
        for v in abcde.values():
            if i == v:
                continue
        abcde[character] = i
        try_all_recursive(lop, rop, rhs, abcde, remaining)


def get_values(lop, rop, rhs):
    uniques = dict()
    for char in lop + rop + rhs:
        uniques[char] = 1

    to_try = list(uniques.keys()) # subset of {a,b,c,d,e}
    abcde = {"a":-1,"b":-1,"c":-1,"d":-1,"e":-1}
    try_all_recursive(lop, rop, rhs, abcde, to_try)

    print("impossible")


def main():
    line = input()
    (lhs, rhs) = line.split("=")
    (lop, rop) = lhs.split("+")

    # lop + rop = rhs

    vals = get_values(lop, rop, rhs)
    for i in range(len(vals)):
        vals[i] = str(vals[i])

    print("".join(vals))


if __name__=="__main__":
    main()
