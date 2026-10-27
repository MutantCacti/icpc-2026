
def impossible():
    print("impossible")
    exit(0)


def main():
    line = list(input())
    line_chars = []
    line_char_ids = []
    for i,char in enumerate(line):
        if char in ("(", ")"):
            continue
        else:
            line_chars.append(char)
            line_char_ids.append(i)

    print("CHARS", "".join(line_chars))

    counts = dict()
    for char in line:
        try:
            counts[char] += 1
        except KeyError:
            counts[char] = 1

    if counts["("] != counts[")"]:
        impossible()

    _sum = 0
    n = 0
    for k,v in counts.items():
        if k not in ("(", ")"):
            _sum += v
            n += 1

    if _sum % 3 != 0:
        impossible()

    # Check 1: at least a third inside shared brackets

    third = n // 3
    for i in range(third - 1, len(line_chars)):
        work = line.copy()

        lb = line_char_ids[i-third-1]
        ub = line_char_ids[i-1]+1

        _slice = work[lb:ub]
        print("SLICE","".join(_slice))

        for i in range(lb, ub):
            if work[i] == "(":
                work2 = work.copy()
                for j,close in enumerate(work[i+1:]):
                    if close == ")":
                        try:
                            work2.pop(j)
                            work2.pop(i)
                        except IndexError:
                            print("INDEXERROR","".join(work2), i, j)




if __name__=="__main__":
    main()
