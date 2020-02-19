from math import *

number, width = eval(input())

def mult_table(N, M):
    digit, max_digit = len(str(N)), len(str(N*N))
    string = '{:>{digit}d} * {:<{digit}d} = {:<{max_digit}d}'
    len_of_string = len(string.format(0, 0, 0 * 0, digit = digit, max_digit = max_digit))
    len_of_symbol = len(' | ')
    max_column = floor((M + len_of_symbol)/(len_of_string + len_of_symbol))
    print('=' * M)
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
