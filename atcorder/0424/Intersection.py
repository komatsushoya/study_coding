N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

target = 0
list = []
min = 100
for i in range(0,N):
    if min > (B[i] - A[i]):
        min = B[i] - A[i]
        target = i
for i in range(A[i],B[i]+1):
    list.append(i)
for l in range(0,N):
    m = 0
    while m < len(list):
        if A[l] > list[m]:
            list.pop(m)
            continue
        elif B[l] < list[m]:
            list.pop(m)
            continue
        m += 1
#print(list)
print(len(list))