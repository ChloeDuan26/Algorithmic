s = input()
n = len(s)

bag = set()
for c in s:
    bag.add(c)

max_cnt = len(bag)
up, down = 1, 1
for i in range(1, n + 1):
       up = up * i
for i in range(1, max_cnt + 1):
       down = down * i  
k = int(up / down)
print(k)