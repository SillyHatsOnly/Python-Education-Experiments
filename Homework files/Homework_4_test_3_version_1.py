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

def maxfun(Sequence, *functions):
    max_sum = 0
    for func in functions:
        list_of_func_val = []
        for arg in Sequence:
            list_of_func_val.append(func(arg))
        if sum(list_of_func_val) > max_sum:
            max_sum = sum(list_of_func_val)
            max_sum_func_index = func
    return max_sum_func_index
