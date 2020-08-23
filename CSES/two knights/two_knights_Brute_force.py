def solve(k):
    cnt = 0
    def count(i, j, k):
        cnt, offset = 0, []
        for a in [-1, +1]:
            for b in [-2, +2]:
                offset.append([a, b])
                offset.append([b, a])
        for da, db in offset:
            if 0 <= (i + da) < k and 0 <= (j + db) < k:
                cnt += 1
        return cnt
    for i in range(k):
        for j in range(k):
            cnt += k * k - 1 - count(i, j, k)
    
    return int(cnt / 2)

n = int(input())
for i in range(1, n + 1):
    print(solve(i))