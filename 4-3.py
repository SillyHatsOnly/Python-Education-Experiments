def maxfun(S, *func):
    max_sum = 0
    for i in func:
        list_of_func_val = []
        for j in S:
            list_of_func_val.append(i(j))
        if sum(list_of_func_val) > max_sum:
            max_sum = sum(list_of_func_val)
            max_sum_func_index = i
    print(max_sum_func_index)
