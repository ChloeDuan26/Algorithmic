def subarraySum(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 1:
            n = int(3 * n + 1)    
        else:
            n = int(n / 2)
        sequence.append(n)
    return sequence

a = subarraySum(int(input()))
for x in range(len(a)): 
    print(a[x])

