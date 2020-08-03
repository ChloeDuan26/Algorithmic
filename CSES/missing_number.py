def subarraySum(nums, n):
    list_a = []
    for i in range(n): 
        list_a.append(0)
    for i in range(n - 1):
        list_a[nums[i] - 1] = 1
    
    return [j + 1 for j in range(n) if list_a[j] == 0][0]

n = int(input())
nums = [int(s) for s in input().split(" ")]
print(subarraySum(nums, n))

