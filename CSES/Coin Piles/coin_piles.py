def solve(a, b):
    if a and b and 2 * b - a >= 0 and (2 * b - a) % 3 == 0 and 2 * a - b >= 0 and (2 * a - b) % 3 == 0: print("YES")
    elif a == 0 and b == 0: print("YES")
    else: print("NO")
    return

n = int(input())
nums = []
for i in range(n):
    nums.append([int(s) for s in input().split(" ")])
for i in range(n):
    solve(nums[i][0], nums[i][1])
