'''
Вводится строка — формула некоторой функции от x. В следующей строке вводятся
через запятую два числа, A и B, такие что f(x) на [A,B] непрерывна,
дифференцируема и имеет ровно один корень, будучи разных знаков на концах
отрезка (проверять не надо). Найти и вывести этот корень с точностью 0.000001
(представление может быть любым). При вычислении f(x) (с помощью eval)
предполагается, что в текущем пространстве имён присутствуют математические функции.

Пример:
Input:
sin(x+0.00007)
-1,2
Output:
-7.033348083496094e-05
'''
from sympy import diff,symbols
from math import *

x, y = symbols('x y')
input_func = eval(input())
a,b = int(eval(input()))


diff_func = diff(input_func())
answer = (diff_func(b) - diff_func(a)) / b - a
