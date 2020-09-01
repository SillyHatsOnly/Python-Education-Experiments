'''
Написать генератор-декоратор statcounter(), который конструирует объекты
(назовём один из них stat) со следующим поведением:
- первый вызов next(stat) возвращает словарь, в котором stat будет хранить
информацию вида ФУНКЦИЯ: КОЛИЧЕСТВО ВЫЗОВОВ, где ФУНКЦИЯ — это исходный
(не обёрнутый) объект-функция
- все последующие вызовы stat.send(function) оборачивают вызов произвольной
функции function увеличением на 1 соответствующего элемента словаря.
Глобальными именами пользоваться нельзя.

Input:
stat = statcounter()
stats = next(stat)

@stat.send
def f1(a): return a+1

@stat.send
def f2(a, b): return f1(a)+f1(b)

print(f1(f2(2,3)+f2(5,6)))
print(stats)

Output:
21
{<function f2 at 0x7fc3151ebb90>: 2, <function f1 at 0x7fc315283e60>: 5}
'''

def statcounter():
    out_dict = dict()
    new = yield out_dict
    while True:
        def fun(f):
            def calc(*args):
                if f in out_dict: out_dict[f] += 1
                else: out_dict[f] = 1
                return f(*args)
            return calc
        new = yield fun(new)

        
stat = statcounter()
stats = next(stat)

@stat.send
def f1(a): return a+1

@stat.send
def f2(a, b): return f1(a)+f1(b)

print(f1(f2(2,3)+f2(5,6)))
print(stats)
