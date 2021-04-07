A = int(input())
B = int(input())
C = int(input())
X = int(input())
i = j = count = 0

max_num_A = X // 500
while i <= min(max_num_A, A):
    rest1 = X - 500 * i
    max_num_B = rest1 // 100
    while j <= min(max_num_B, B):
        rest2 = rest1 - 100 * j
        max_num_C = rest2 // 50
        if rest2 % 50 == 0 and rest2 <= (50 * C):
            count += 1
        j += 1
    i += 1
    j = 0
print(count)
