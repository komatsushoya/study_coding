import copy

N = int(input()) // 2
S = input()  # 入力文字列
Q = int(input())  # クエリの個数
T = [list(map(int, input().split())) for i in range(Q)]
S2 = S
S2_new = []
for j in range(Q):
    if T[j][0] == 1:
        a = S2[T[j][1] - 1]
        b = S2[T[j][2] - 1]
        S2_new.clear()
        for k in range(len(S)):
            if k == T[j][1]-1:
                S2_new.append(b)
            elif k == T[j][2]-1:
                S2_new.append(a)
            else:
                S2_new.append(S2[k])
        S2 = copy.copy(S2_new)
    elif T[j][0] == 2:
        a = S2[:N + 1]
        b = S2[N + 1:]
        S2 = b + a
print(''.join(S2))
