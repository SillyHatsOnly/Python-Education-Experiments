input_number = int(input())
copy_of_number = input_number
orders_count = 1

if input_number < 10 or input_number == 0:
    print("NO")

while copy_of_number > 10:
    copy_of_number = copy_of_number // 10
    orders_count += 1

number_as_array = [0]
array_index_count = 0
copy_of_number = input_number

while orders_count > 0:
    number_as_array.append(
        (copy_of_number - (number_as_array[array_index_count]*10**orders_count))
        // 10**(orders_count-1))
    copy_of_number = copy_of_number
                     - (number_as_array[array_index_count]*10**orders_count)
    orders_count -= 1
    array_index_count += 1

number_as_array.pop(0)
len_of_array = len(number_as_array)
array_index_count = 0
victory = True

while array_index_count < len_of_array:
    if number_as_array[array_index_count] != number_as_array[-(array_index_count+1)]:
        print("NO")
        victory = False
        break
    else:
        array_index_count += 1

if victory:
    print("YES")
