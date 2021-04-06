N = int(input())
L = list(map(int, input().split()))
count = 0
def do_exit():
    print(count)
    exit()
while True:
    for i in range(N):
        if L[i]!=0 and L[i]%2==0:
            L[i] = L[i] / 2
        else:
            do_exit()
    count += 1
