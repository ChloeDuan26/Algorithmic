def dice_combination(n):
    if n < 0: return 0
    if n == 0: return 0
    count = [0] * (n + 1)
    count[0] = 1
    for i in range(1, n + 1):
        for j in range(1, 7):
            if i - j >= 0:
                count[i] += count[i - j]
                count[i] %= int(1e9 + 7)
            else:
                break
            
    return count[n]

n = int(input())
print(dice_combination(n))

