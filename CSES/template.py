def subarraySum(nums, n, k):
    pre, last, sum_sub, num = 0, 0, nums[0], 0
    while last+1 <= n:
        if sum_sub == k:
            num += 1
            #print (pre)
            #print (last)
            if pre != last:
                sum_sub = sum_sub - nums[pre]
                pre += 1
            else:
                while (last+1 < n) and (nums[last+1] > k):
                    last += 1
                if last+1 == n:
                    return num
                last += 1
                pre = last
                sum_sub = nums[pre]
        else:
            if (last+1 < n) and (sum_sub + nums[last+1] <= k):
                last += 1
                sum_sub = sum_sub + nums[last]
            else:
                while (last+1 < n) and (nums[last+1] > k):
                    last += 1
                if last+1 == n:
                    return num
                last += 1
                pre = last
                sum_sub = nums[pre]
    #print (last) 
    return num

n, k = [int(s) for s in input().split(" ")]
nums = [int(s) for s in input().split(" ")]

print(subarraySum(nums, n, k))

