N,A,B = map(int, input().split())
count = 0
def amari(_i,size):
    X = _i // size
    _i -= size * X
    return X, _i

for i in range(1,N+1):
    j = i
    X1,j = amari(j,10000)
    X2,j = amari(j,1000)
    X3,j = amari(j,100)
    X4,j = amari(j,10)
    sum = X1 + X2 + X3 + X4 + j
    if A <= sum and sum <= B:
        count += i
print(count)