'''
Написать функцию-параметрический декоратор fix(n), с помощью
которой все вещественные (как позиционные, так и именные)
параметры произвольной декорируемой функции, а также её
возвращаемое значение, округляются до n-го знака после запятой.
Если какие-то параметры функции оказались не вещественными, или
не вещественно возвращаемое значение, эти объекты не меняются.

Input:
@fix(4)
def aver(*args, sign=1):
    return sum(args)*sign

print(aver(2.45675901, 3.22656321, 3.432654345, 4.075463224, sign=-1))

В примере входные данные округляются до 2.4568, 3.2266, 3.4327, 4.0755,
затем складываются, затем снова округляются. sign не преобразуется
(хотя этого и не видно :)), потому что он не вещественный.

Output:
-13.1916
'''

def fix(n):
    def newfun(func):
        def function(*args, sign):
            tmp = list()
            for i in args:
                if type(i) == float:
                    tmp.append(round(i, n))
                else:
                    tmp.append(i)
            return round(sum(tmp)*sign, n) if type(sign) != float else round(sum(tmp)*round(sign, n), n)
        return function
    return newfun

@fix(6)
def aver(*args, sign=1):
    return sum(args)*sign

print(aver(2.45675901, 3.22656321, 3.432654345, 4.075463224, sign=-1))
