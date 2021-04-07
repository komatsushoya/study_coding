N = int(input())
L = sorted(list(map(int, input().split())), reverse=True)
A = B = 0
for i in range(len(L)):
    if i % 2 == 0:
        A += L[i]
    elif i % 2 == 1:
        B += L[i]
print(A - B)
