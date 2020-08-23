s = input()
dic = {}

for c in s:
    if c in dic:
        dic[c] += 1
    else:
        dic[c] = 1
    
flag = True 
odd_cnt = 0
odd_value = ''
for c, v in dic.items():
    if v % 2 == 1:
        odd_cnt += 1
        odd_value = c
        if odd_cnt == 2:
            flag = False
            break

a = ''
if not flag:
    print("NO SOLUTION")
else:
    for c, v in dic.items():
        a += c * (v // 2)
    b = a[::-1]
    a += odd_value
    a += b
    print(a)

