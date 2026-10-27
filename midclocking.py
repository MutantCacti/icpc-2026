
def get_minimum_time(s, n, m1, sds):
    s2 = s - m1
    n2 = n - m1
    m2 = 2 * (s2 - n2) - 1
    m3 = n - m1 - m2

    assert m1 + m2 + m3 == n

    for i,d in enumerate(sds):
        if i < m1:
            continue
        elif i < m2:
            sds[i] /= 0.6
        else:
            sds[i] /= 0.3

    # print(sds)
    # print(str(m1)+"m1", str(m2)+"m2", str(m3)+"m3", sds)
    return max(sds)


def main():
    line1 = input().split()
    (n, s) = (int(line1[0]), int(line1[1]))

    line2 = input().split()
    durations = []
    for t in line2:
        durations.append(int(t))

    sorted_durations = sorted(durations, reverse=True)
    # print(sorted_durations)

    gaps = s - n
    min_time = -1

    for i in range(0, gaps + 1):
        # print(i)
        t = get_minimum_time(s, n, i, sorted_durations.copy())
        if min_time == -1 or t < min_time:
            min_time = t

    print(min_time)


if __name__=="__main__":
    main()
