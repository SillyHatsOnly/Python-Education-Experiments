'''
Ввести небольшое натуральное число 2 ⩽ N ⩽ 1000000 и проверить, является ли оно степенью натурального числа (>1).
Вывести YES или NO соответственно.

Пример:
Input: 1024
Output: YES
'''

import math
input_number = int(input())
count = 2
right_result = False
if input_number < 2 or input_number > 1000000:
    print("ERROR")
else:
    while count < input_number:
        result = math.modf(input_number**(1/count))
        if result[0] == 0:
            print("YES")
            right_result = True
            break
        count += 1
    if right_result == False:
        print("NO")
