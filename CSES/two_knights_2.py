import numpy as np

def two_knights(demo, k):
    cnt = 0
    for i in range(k):
        for j in range(k):
            demo_2 = np.ones((5,5))
            list_ = [i, j, k - 1 - i, k - 1 - j]
            
            if list_[0] == 1: demo_2[0] = 0
            if list_[0] == 0: demo_2[0:2] = 0
                
            if list_[1] == 1: demo_2[:,0] = 0
            if list_[1] == 0: demo_2[:,0:2] = 0

            if list_[2] == 1: demo_2[4] = 0
            if list_[2] == 0: demo_2[3:5] = 0

            if list_[3] == 1: demo_2[:,4] = 0
            if list_[3] == 0: demo_2[:,3:5] = 0
            
            dot = demo * demo_2
            ccnt = k * k - np.sum(dot == 1)
            cnt += ccnt
    return cnt // 2


demo = np.array([[0,1,0,1,0],[1,0,0,0,1],[0,0,1,0,0],[1,0,0,0,1],[0,1,0,1,0]])
n = int(input())
for i in range(1, n + 1):
    print(two_knights(demo, i))
