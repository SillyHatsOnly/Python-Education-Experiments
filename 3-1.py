test_list = [int(input())]

def max_sum_of_list(new_list, max_sum = 0, sum_list = 0):
    for i in new_list:
        sum_list = sum_list + i
        if sum_list > max_sum:
            max_sum = sum_list
    if len(new_list) < 1:
        return print(max_sum)
    new_list.pop(0)
    max_sum_of_list(new_list, max_sum, sum_list = 0)

while test_list[-1] != 0:
    test_list.append(int(input()))

if test_list[0] == 0:
    print('Wrong number!')

max_sum_of_list(test_list)
