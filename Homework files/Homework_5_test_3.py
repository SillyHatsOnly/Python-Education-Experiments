'''
Пользуясь формулой Лейбница для вычисления числа Пи:
pi/4 = 1/1 - 1/3 + 1/5 -1/7 + 1/9 - 1/11 + ...
написать бесконечный генератор pigen(), возвращающий
последовательно 4, 4-4/3, 4-4/3+4/5, 4-4/3+4/5-4/7…;

Пример:
Input:
P=pigen()
print(next(P), next(P), next(P), next(P), sep="\n")
Output:
4.0
2.666666666666667
3.466666666666667
2.8952380952380956
'''

from math import *
def pigen():
    numerator = 4
    denominator = 1
    sum_of = numerator/denominator
    while True:
        yield sum_of
        denominator += 2
        sum_of -= numerator/denominator
        yield sum_of
        denominator += 2
        sum_of += numerator/denominator
