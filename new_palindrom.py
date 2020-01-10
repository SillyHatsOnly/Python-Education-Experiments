input_number = int(input())
copy = input_number
reverse_number = 0
while copy > 0:
    remainder_of_division = copy % 10
    copy = copy // 10
    reverse_number = reverse_number*10
    reverse_number = reverse_number + remainder_of_division
if input_number == reverse_number:
    print("YES")
else:
    print("NO")
