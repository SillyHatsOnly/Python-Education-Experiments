string = int(input())
column = int(input())
x, y, count = 0, 0, 0
string_max, column_max = string, column
string_min, column_min = 0, 0

matrix = [[-1 for x in range(column)] for y in range(string)]

for i in range(string*column):

    if x < column_max and y == string_min:
        matrix[y][x] = count
        x += 1
        if x == column_max:
            column_max = column_max - 1
            x = column_max
            y += 1
        count += 1
        if count > 9:
            count = 0

    elif x == column_max and y < string_max:
        matrix[y][x] = count
        y += 1
        if y == string_max:
            string_max = string_max - 1
            y = string_max
        count += 1
        if count > 9:
            count = 0

    elif y == string_max and x <= column_max:
        x -= 1
        matrix[y][x] = count
        if x == column_min:
            column_min = column_min + 1
            y -= 1
        count += 1
        if count > 9:
            count = 0
        
    elif x < column_min and y >= string_min:
        matrix[y][x] = count
        y -= 1
        if y == string_min:
            string_min = string_min + 1
            y = string_min
            x += 1
        count += 1
        if count > 9:
            count = 0
for i in matrix:
    print(*i)
