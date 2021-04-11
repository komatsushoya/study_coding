import math

R, X, Y = map(int, input().split())
distance = math.sqrt(X * X + Y * Y)
if distance < R:
    print(2)
    exit()
elif distance % R == 0:
    print(int(distance / R))
    exit()
else:
    print(int(distance // R + 1))
    exit()
