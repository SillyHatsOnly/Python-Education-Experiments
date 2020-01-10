from math import *
input_number = int(input())
first_count = 2
second_count = 2
victory = False

if 2 > input_number or input_number > 1000000:
    print("ERROR")
else:
    while first_count < input_number:
        while second_count < input_number:
            if log(input_number, first_count) == second_count:
                victory = True
                print("YES")
                break
            second_count += 1
        first_count += 1
    if victory == False:
        print("NO")
