
def main():
    n = int(input())

    n_factors = []
    for i in range(1, n+1):
        if (n % i) == 0:
            n_factors.append(i)

    x = -1
    for i in n_factors:
        for j in n_factors:
            product = i * j
            if product < n and product > x:
                x = product

    a = n + x
    b = n + (n*n // x)

    print(a, b)

if __name__=="__main__":
    main()
