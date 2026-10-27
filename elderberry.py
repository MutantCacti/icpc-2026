def weight(a, b, c):
    return (a / 3, b / 3, c / 10)


def main():
    line = input().split()
    (eb, su, wa) = (float(line[0]), float(line[1]), float(line[2]))

    a, b, c = weight(eb, su, wa)

    m = min(a, b, c)

    a -= m
    b -= m
    c -= m

    la = max(a, b, c)

    add = [(la - a) * 3, (la - b) * 3, (la - c) * 10]

    for i,v in enumerate(add):
        if int(v) == v:
            add[i] = int(v)
        add[i] = str(add[i])

    print(" ".join(add))


if __name__=="__main__":
    main()
