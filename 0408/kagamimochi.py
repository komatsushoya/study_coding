N = int(input())
L = []
count = beforeN = 0
for i in range(N):
    L.append(int(input()))
L = sorted(L)

for i in range(N):
    if L[i] > beforeN:
        count += 1
        beforeN = L[i]
print(count)