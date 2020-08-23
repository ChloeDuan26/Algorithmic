def num_spiral(y, x):
    if y >= x:
        if y % 2 == 0: return y * y - x + 1
        else: return (y - 1) * (y - 1) + x
    else:
        if x % 2 == 1: return x * x - y + 1
        else: return (x - 1) * (x - 1) + y

n = int(input())
x, y = [1] * n, [1] * n
for i in range(n):
    y[i], x[i] = [int(s) for s in input().split(" ")]
for i in range(n):
    print(num_spiral(y[i], x[i]))
    