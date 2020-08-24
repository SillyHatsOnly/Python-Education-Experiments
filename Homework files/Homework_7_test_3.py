'''
Написать функцию checkhash(seq, f, mod), которой на вход
подаётся последовательность неравных друг другу (это
гарантируется) хешируемых объектов, хеш-функция и число mod.
Функция формирует новую редуцированную хеш-функцию r()=f()%mod,
и собирает статистику коллизий по каждому значению r() на
исходной последовательности. checkhash(seq, f, mod) возвращает
кортеж из двух элементов — наибольшее и наименьшее количество
произошедших коллизий.

Input:
from math import *
print(checkhash(range(-1000000,1000000,77),hash,128))
print(checkhash(range(-1000000,1000000,77),lambda x: int(f"{sin(x+1):14.13f}"[-5:]),128))

Output:
(204, 202)
(260, 112)
'''
from collections import Counter

def checkhash(seq, f, mod):
    a = Counter([f(i)%mod for i in seq])
    return max(a.values()), min(a.values())
