def subarraySum(n, x, nums):
    l, r, sum_sub, num = 0, -1, 0, 0
    len_nums = len(nums)
    for l in range(len_nums):
        while (r + 1 < len_nums) and (sum_sub + nums[r + 1] <= x): 
            r += 1
            sum_sub += nums[r] 
        if sum_sub == x: num += 1
        if r >= l: sum_sub -= nums[l]
        else: r = l

    return num

n, x = [int(s) for s in input().split(" ")]
nums = [int(s) for s in input().split(" ")]
print(subarraySum(n, x, nums))