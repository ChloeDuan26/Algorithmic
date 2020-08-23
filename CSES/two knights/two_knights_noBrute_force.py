def solve(k):
    cnt = [0, 0, 6, 28, 96]
    if 1 <= k <= 4: return cnt[k]

    cnt, k_2 = 0, k * k
    cnt += (k_2 - 9) * (k - 4) * (k - 4)
    cnt += (k_2 - 3) * 4
    cnt += (k_2 - 4) * 8
    cnt += (k_2 - 5) * (k - 3) * 4
    cnt += (k_2 - 7) * (k - 4) * 4

    return int(cnt / 2)

n = int(input())
for i in range(1, n + 1):
    print(solve(i))