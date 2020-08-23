def two_sets(n):
    sum_set = (1 + n) * n /2
    if sum_set % 2 == 1:
        print("NO")
    else:
        half_sum = sum_set /2
        cnt, list_1, list_2 = 0, [], []
        for i in range(n):
            if n - i <= half_sum and cnt + (n - i) <= half_sum:
                cnt += n - i
                list_1.append(n - i)
            else:
                list_2.append(n - i)
        print("YES")
        len_list_1 = len(list_1)
        print(len_list_1)
        print(" ".join(str(list_1[len_list_1 - 1 - i]) for i in range(len_list_1))) 
        len_list_2 = len(list_2)
        print(len_list_2)
        print(" ".join(str(list_2[len_list_2 - 1 - i]) for i in range(len_list_2))) 
    return 

n = int(input())
two_sets(n)