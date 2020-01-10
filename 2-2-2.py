import math
input_number = int(input())
count = 2
victory = False

if 2 > input_number or input_number > 1000000:
    print("ERROR")
else:
    while count < input_number:
        result = math.modf(input_number**(1/count))
        if result[0] == 0:
            print("YES")
            victory = True
            break
        count += 1
    if victory == False:
        print("NO")
