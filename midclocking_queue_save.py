
def get_minimum_time_2(s, m1, m2, sds):
    m3 = s - 2 * m1 - 3 * m2

    if m3 > 2:
        pass
    elif m3 == 2:
        m2 += 2
        m3 = 0
    elif m3 == 1:
        m1 += 1
        m3 = 0
    else:
        m3 = 0

    num_p = m1 + m2 + m3
    accum = []
    multi = []
    leftover = []

    for i in range(len(sds)):
        if i < num_p:
            accum.append(sds[i])
            if i < m1:
                multi.append(1)
            elif i < m1 + m2:
                multi.append(1 / 0.6)
            else:
                multi.append(1 / 0.3)
        else:
            leftover.append(sds[i])

    # accum = [0, 1, 2, 3, 4, 5]
    # multi = [1, 1, 1, 1, 0.6, 0.6]
    # leftover = [6, 7, 8, 9]

    for i in range(len(accum)):
        accum[i] *= multi[i]

    while len(leftover) != 0:
        _next = leftover.pop(0)
        first_done_idx = accum.index(min(accum))
        accum[first_done_idx] += _next * multi[first_done_idx]

    print(sds)
    print(str(m1)+"m1", str(m2)+"m2", str(m3)+"m3", accum)
    return max(accum)


def get_minimum_time_1(s, n, m1, sds):
    s2 = s - (2 * m1)

    min_time = -1
    possible_m2 = int((2 * s2 + 1) / 3)

    for i in range(0, possible_m2, 2):
        t = get_minimum_time_2(s, m1, i, sds.copy())
        if min_time == -1 or t < min_time:
            min_time = t

    return min_time


def main():
    line1 = input().split()
    (n, s) = (int(line1[0]), int(line1[1]))

    line2 = input().split()
    durations = []
    for t in line2:
        durations.append(int(t))

    sorted_durations = sorted(durations, reverse=True)
    print(sorted_durations)

    min_time = -1
    possible_m1 = int((s + 1) / 2)

    for i in range(0, possible_m1):
        t = get_minimum_time_1(s, n, i, sorted_durations.copy())
        if min_time == -1 or t < min_time:
            min_time = t

    print(min_time)


if __name__=="__main__":
    main()
