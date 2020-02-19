N, M = eval(input())
# N - вывести таблицу умножения от 1 до N включительно
# M - максимальная ширина строки, в которую надо вписать столбцы (но не меньше ширины одного столбца)

orders = len(str(N))
max_orders = len(str(N*N))

string = '{:>{orders}d} * {:<{orders}d} = {:<{max_orders}d}'
new_string_arr = []
print('='*M)
for i in range(1, N+1):
    for j in range(1, N+1):
        new_string_arr.append(string.format(j, i, j*i, orders = orders, max_orders = max_orders))
for i in new_string_arr:
    print(i, end=' | \n')
