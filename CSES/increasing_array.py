def increasing_array(n, nums):
    x = 0
    for i in range(0, n - 1):
        if nums[i + 1] < nums[i]:
            x += nums[i] - nums[i + 1]
            nums[i + 1] = nums[i]

    return x 

n = int(input())
nums = [int(s) for s in input().split(" ")]
print(increasing_array(n, nums))
