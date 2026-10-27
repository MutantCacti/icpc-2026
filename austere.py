
def get_most_common_char(d):
    _mk = None
    _max = -1
    for k,v in d.items():
        if v > _max:
            _mk = k
            _max = v
    if _mk is None:
        return 'a'
    return _mk


def main():
    line1 = input().split()
    (n, k) = (int(line1[0]), int(line1[1]))

    line2 = input()
    words = line2.split()

    counts = dict()

    for word in words:
        for char in word:
            try:
                counts[char] += 1
            except KeyError:
                counts[char] = 1

    kept = []
    for i in range(k):
        new_c = get_most_common_char(counts)
        kept.append(new_c)
        counts.pop(new_c)

    for i,word in enumerate(words):
        for j,char in enumerate(word):
            if char in kept:
                continue
            else:
                word_chars = list(words[i])
                word_chars[j] = kept[0]
                words[i] = "".join(word_chars)

    final = " ".join(words)
    print(final)


if __name__=="__main__":
    main()