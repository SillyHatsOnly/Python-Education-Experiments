N, M = eval(input())
# N - вывести таблицу умножения от 1 до N включительно
# M - максимальная ширина строки, в которую надо вписать столбцы (но не меньше ширины одного столбца)

orders = len(str(N))
max_orders = len(str(N*N))

string = '{:>{orders}d} * {:<{orders}d} = {:<{max_orders}d}'
max_len_of_N = len(string.format(0, 0, 0*0, orders = orders, max_orders = max_orders))
max_column = int(M / max_len_of_N)
sum_of_len = 0

print('='*M)
for line in range(1, N+1, max_column):
    for j in range(1, N+1):
        for i in range(line, min(line+max_column, N+1)):
            print(string.format(i, j, i*j, orders = orders, max_orders = max_orders), end = '')
            sum_of_len += len(string.format(i, j, i*j, orders = orders, max_orders = max_orders ))
            if (sum_of_len + len(" | ")) <= M:
                sum_of_len += len(' | ')
                print(' | ', end = '')
            else:
                sum_of_len = 0
                print('\n', end = '')
    print('='*M)
