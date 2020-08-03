def repetitions(dnaStr):
    len_rep, num = 0, 0
    x = dnaStr[0]
    for i in range(len(dnaStr)):
        if i != 0 and x == dnaStr[i]:
            #print('enter')
            num += 1
            if i == len(dnaStr) - 1 and len_rep < num: len_rep = num 
        else: 
            x = dnaStr[i]
            if len_rep < num: 
                len_rep = num 
                num = 0
        
    return len_rep + 1

dnaStr = input()
print(repetitions(dnaStr))