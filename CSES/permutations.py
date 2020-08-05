def permutations(n):
    if n == 2 or n == 3: return 0
    list_n = [1] * n
    x = n // 2
    list_n[x] = n
    if n % 2 == 1:
        for i in range(x):
            list_n[x + 1 + i] = 2 + 2 * i
            list_n[x - 1 - i] = 1 + 2 * i
    else:
        for i in range(x - 1):
            list_n[x + 1 + i] = 2 + 2 * i
            list_n[x - 1 - i] = 1 + 2 * i
        list_n[0] = n - 1

    return list_n

n = int(input())
if permutations(n): print(" ".join(str(i) for i in permutations(n))) 
else: print('NO SOLUTION')
