'''
Ввести целое положительное число и проверить, является ли оно палиндромом,
т. е. совпадает ли первая цифра с последней, вторая — с предпоследней и т. д.
Представлять число в виде последовательности (строки, списка и т. п.) нельзя.
Вывести YES или NO соответственно. Лидирующие нули не учитывать (числа,
заканчивающиеся на 0 — автоматически не палиндромы).

Пример:
Input:  1234321
Output: YES
'''

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
