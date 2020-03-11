'''
Написать функцию maxfun(), которая принимает переменное число параметров —
числовую последовательность S, функцию F1 и, возможно, ещё несколько
функций F2 … Fn. Возвращает она ту из функций Fi, сумма значений которой
на всех элементах S наибольшая. Если таких функций больше одной,
возвращается Fi с наибольшим i.

Input:
from math import *
print(maxfun(range(-2,10), sin, cos, exp)(1))
Output: 2.718281828459045
'''

from math import *

def maxfun(S, *F):
    return F[max(enumerate(sum(f(x) for x in S) for f in F), key=lambda x: x[1])[0]]
