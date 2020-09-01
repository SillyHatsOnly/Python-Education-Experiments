'''
Написать функцию-декоратор nonify(func), которая заменяет
возвращаемое значение функции func на None, если оно было
пустое (и не меняет в противном случае).

Input:
@nonify
def aNb(a, n, b):
    return a*n+b

print(aNb(1,2,3), aNb("QWE",0,""))

Output:
5 None
'''

def nonify(f):
    def newfun(*args):
        if f(*args) == '' or f(*args) == 0:
            return 'None'
        else:
            return f(*args)
    return newfun

@nonify
def aNb(a, n, b):
    return a*n + b

print(aNb(1,2,3), aNb('QWE',0,""))
