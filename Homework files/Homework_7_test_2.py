'''
Ввести построчно четвёрки вида «число число число слово», где первые три числа —
это координаты галактики по имени «слово» (некоторые галактики могут называться
одинаково, но координаты у всех разные). Последняя строка ввода не содержит
пробелов и не учитывается. Вывести в алфавитном порядке имена любых двух наиболее
удалённых друг от друга галактик.

Пример:
Input:
35.764 -797.636 -770.320 almost
88.213 -61.688 778.457 gene
-322.270 -248.555 -812.730 trend
721.262 630.355 968.287 dow
-895.519 -970.173 97.282 non
-561.036 -350.840 -723.149 disco
-151.546 -900.962 -658.862 bidder
-716.197 478.576 -695.843 hawaii
-744.664 -173.034 -11.211 sad
-999.968 990.467 650.551 erik
.
Output:
almost erik
'''
from math import *

def galaxy():
    Dict = {}
    count = 0
    while True:
        val = input()
        input_values = val.split(' ')
        if len(input_values) == 1:
            break
        x, y, z, galaxy_name = input_values
        x, y, z = float(x), float(y), float(z)
        Dict[count] = [x,y,z,galaxy_name]
        count += 1
    dist_set = {}
    for first_val in Dict.items():
        f_count, f_data = first_val
        f_x,f_y,f_z,f_name = f_data
        for second_val in Dict.items():
            s_count, s_data = second_val
            s_x,s_y,s_z,s_name = s_data
            max_dist = sqrt((s_x - f_x)**2 + (s_y - f_y)**2 + (s_z - f_z)**2)
            if f_count != s_count:
                dist_set.setdefault(max_dist, (f_name, s_name))
    print(*dist_set[max(dist_set)])
        
galaxy()
