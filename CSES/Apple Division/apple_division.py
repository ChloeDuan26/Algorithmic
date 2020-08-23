n = int(input())
weights = [int(s) for s in input().split(" ")]

sum = 0
for w in weights:
    sum += w
half_sum = sum / 2

weights.sort()
i, cnt = n - 1, 0
less = False
while True:
    if cnt + weights[i] < half_sum:
        if less:
            cnt_min = half_sum - cnt - weights[i]
            cnt_max = cnt + weights[i + 1] - half_sum
            print(int(min(cnt_min, cnt_max) * 2))
            break
        cnt += weights[i]
        i -= 1
    else:
        i -= 1
        less = True





