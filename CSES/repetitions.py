def repetitions(dnaStr):
    len_rep, num = 1, 1
    for i in range(0, len(dnaStr) - 1):
        if dnaStr[i] == dnaStr[i + 1]:
            num += 1
            len_rep = max(len_rep, num)
        else: 
            len_rep = max(len_rep, num)
            num = 1
        
    return len_rep

dnaStr = input()
print(repetitions(dnaStr))