'''
Ввести два натуральных числа через запятую: N и M. Вывести таблицу
умножения от 1 до N включительно в формате, представленном ниже.
Количество столбцов в выводе должно быть наибольшим, но общая ширина
строки не должна превышать M (предполагается, что M достаточно
велико, чтобы вместить один столбец). Ширина колонок под сомножители
и произведения должна соответствовать максимальной ширине
соответствующего значения (даже если в данной колонке данного столбца
эта ширина не достигается, см. пример). Таким образом все столбцы
должны быть одинаковой ширины, без учёта пробелов в конце строк,
которых быть не должно. Разделители вида "===…===" должны быть ширины M.

Пример:
Input:  11, 62
Output:
==============================================================
 1 * 1  = 1   |  2 * 1  = 2   |  3 * 1  = 3   |  4 * 1  = 4  
 1 * 2  = 2   |  2 * 2  = 4   |  3 * 2  = 6   |  4 * 2  = 8  
 1 * 3  = 3   |  2 * 3  = 6   |  3 * 3  = 9   |  4 * 3  = 12 
 1 * 4  = 4   |  2 * 4  = 8   |  3 * 4  = 12  |  4 * 4  = 16 
 1 * 5  = 5   |  2 * 5  = 10  |  3 * 5  = 15  |  4 * 5  = 20 
 1 * 6  = 6   |  2 * 6  = 12  |  3 * 6  = 18  |  4 * 6  = 24 
 1 * 7  = 7   |  2 * 7  = 14  |  3 * 7  = 21  |  4 * 7  = 28 
 1 * 8  = 8   |  2 * 8  = 16  |  3 * 8  = 24  |  4 * 8  = 32 
 1 * 9  = 9   |  2 * 9  = 18  |  3 * 9  = 27  |  4 * 9  = 36 
 1 * 10 = 10  |  2 * 10 = 20  |  3 * 10 = 30  |  4 * 10 = 40 
 1 * 11 = 11  |  2 * 11 = 22  |  3 * 11 = 33  |  4 * 11 = 44 
==============================================================
 5 * 1  = 5   |  6 * 1  = 6   |  7 * 1  = 7   |  8 * 1  = 8  
 5 * 2  = 10  |  6 * 2  = 12  |  7 * 2  = 14  |  8 * 2  = 16 
 5 * 3  = 15  |  6 * 3  = 18  |  7 * 3  = 21  |  8 * 3  = 24 
 5 * 4  = 20  |  6 * 4  = 24  |  7 * 4  = 28  |  8 * 4  = 32 
 5 * 5  = 25  |  6 * 5  = 30  |  7 * 5  = 35  |  8 * 5  = 40 
 5 * 6  = 30  |  6 * 6  = 36  |  7 * 6  = 42  |  8 * 6  = 48 
 5 * 7  = 35  |  6 * 7  = 42  |  7 * 7  = 49  |  8 * 7  = 56 
 5 * 8  = 40  |  6 * 8  = 48  |  7 * 8  = 56  |  8 * 8  = 64 
 5 * 9  = 45  |  6 * 9  = 54  |  7 * 9  = 63  |  8 * 9  = 72 
 5 * 10 = 50  |  6 * 10 = 60  |  7 * 10 = 70  |  8 * 10 = 80 
 5 * 11 = 55  |  6 * 11 = 66  |  7 * 11 = 77  |  8 * 11 = 88 
==============================================================
 9 * 1  = 9   | 10 * 1  = 10  | 11 * 1  = 11 
 9 * 2  = 18  | 10 * 2  = 20  | 11 * 2  = 22 
 9 * 3  = 27  | 10 * 3  = 30  | 11 * 3  = 33 
 9 * 4  = 36  | 10 * 4  = 40  | 11 * 4  = 44 
 9 * 5  = 45  | 10 * 5  = 50  | 11 * 5  = 55 
 9 * 6  = 54  | 10 * 6  = 60  | 11 * 6  = 66 
 9 * 7  = 63  | 10 * 7  = 70  | 11 * 7  = 77 
 9 * 8  = 72  | 10 * 8  = 80  | 11 * 8  = 88 
 9 * 9  = 81  | 10 * 9  = 90  | 11 * 9  = 99 
 9 * 10 = 90  | 10 * 10 = 100 | 11 * 10 = 110
 9 * 11 = 99  | 10 * 11 = 110 | 11 * 11 = 121
==============================================================
'''

from math import *

number, width = eval(input())

def mult_table(N, M):
    digit, max_digit = len(str(N)), len(str(N*N))
    string = '{:>{digit}d} * {:<{digit}d} = {:<{max_digit}d}'
    len_of_string = len(string.format(0, 0, 0 * 0, digit = digit, max_digit = max_digit))
    len_of_symbol = len(' | ')
    max_column = floor((M + len_of_symbol)/(len_of_string + len_of_symbol))
    print('=' * M)
    # от 1 до N с шагом max_column
    for line in range(1, N + 1, max_column):
        for j in range(1, N + 1):
            max_i_val = min(line + max_column, N + 1)
            for i in range(line, max_i_val):
                print_string = string.format(i, j, i * j, digit = digit, max_digit = max_digit)
                if i == max_i_val - 1:
                    print(print_string, end = '\n')
                else:
                    print(print_string, end = ' | ')
        print('=' * M)

mult_table(number, width)
