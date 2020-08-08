class array:
    def _init_(self, k, x):
        self = []
        for i in range(k):
            self.append([x] * k)

    def assignment(self, l, c, value):
        for i in l:
            for j in c:
                self[i][j] = value

def two_knights(demo, demo_2, k):
    cnt = 0
    for i in range(k):
        for j in range(k):
            list_ = [i, j, k - 1 - i, k - 1 - j]
            if list_[0] <= 1: 
                demo_2[0][:] = [0,0,0,0,0]
                if list_[0] == 0:
                    demo_2[1][:] = [0,0,0,0,0]
            if list_[1] <= 1: 
                demo_2[:][0] = [0,0,0,0,0]
                if list_[1] == 0:
                    demo_2[:][1] = [0,0,0,0,0]
            if list_[2] <= 1: 
                demo_2[4][:] = [0,0,0,0,0]
                if list_[2] == 0:
                    demo_2[3][:] = [0,0,0,0,0]
            if list_[3] <= 1: 
                demo_2[:][4] = [0,0,0,0,0]
                if list_[3] == 0:
                    demo_2[:][3] = [0,0,0,0,0]

            dot = [[a*b for a, b in zip(l, m)] for l, m in zip(demo, demo_2)]
            ccnt = 0
            for x in range(5):
                for y in range(5):
                    if dot[x][y] == 1: ccnt += 1
            cccnt = k * k - ccnt
            print(demo_2)
            print(cccnt)
            cnt += cccnt
    return cnt // 2


demo = []
for i in range(5):
    demo.append([0]*5)
demo[0][1], demo[0][3], demo[1][0], demo[1][4], demo[2][2], demo[3][0], demo[3][4], demo[4][1], demo[4][3] = 1, 1, 1, 1, 1, 1, 1, 1, 1

demo_2 = []
for i in range(5):
    demo_2.append([1]*5)

two_knights(demo, demo_2, 3)
#n = int(input())
#for i in range(1, n + 1):
    #print(two_knights(i))