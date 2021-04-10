N, Y = map(int, input().split())
Y /= 1000
for i in range(N + 1):
    for j in range(N + 1 - i):
        if 10 * i + 5 * j + (N - i - j) == Y:
            print(i, j, N - i - j)
            exit()
print("-1 -1 -1")
