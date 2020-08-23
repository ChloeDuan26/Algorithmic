def solve(n):
    cnt, k = 0, 5
    while n // k:
        cnt += n // k
        k *= 5
    return cnt

n = int(input())
print(solve(n))