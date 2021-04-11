N = input()
L = len(N)
count = 0
tmp = int(N)
N2 = []

if N == 0:
    print("Yes")
    exit()

for i in range(9):
    if tmp % 10 == 0:
        count += 1
        tmp /= 10
    else:
        break

N2 = N[0:L - count]
L = len(N2)
for i in range(L // 2):
    if N2[i] != N2[L - 1 - i]:
        print("No")
        exit()
print("Yes")
