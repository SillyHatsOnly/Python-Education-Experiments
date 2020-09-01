'''
Написать параметрический итератор turtle(coord, direction), описывающий движение
«черепахи» по координатной плоскости. coord — это кортеж из двух целочисленных
начальных координат, direction описывает первоначальное направление (0 — восток,
1 — север, 2 — запад, 3 — юг). Координаты увеличиваются на северо-восток. Итератор
принимает три команды — "f" (переход на 1 шаг вперёд), "l" (поворот против часовой
стрелки на 90°) и "r" (поворот по часовой стрелке на 90°) и возвращает текущие
координаты черепахи.

Input:
robo = turtle((0,0),0)
start = next(robo)
for c in "flfrffrffr":
    print(*robo.send(c))

Output:
1 0
1 0
1 1
1 1
2 1
3 1
3 1
3 0
3 -1
3 -1
'''

def turtle(coord, direction):
    x, y = coord
    d = direction
    mlist = [(1,0), (0,1), (-1,0), (0,-1)]
    m = yield coord
    while m:
        xd, yd = mlist[d]
        if m == 'f':
            x = x + xd
            y = y + yd
        elif m == 'r':
            d -= 1
            if d < 0:
                d = 3
        elif m == 'l':
            d += 1
            if d > 3:
                d = 0
        m = yield (x,y)

#другие варианты решения задания (не мои):

##def add_p(p0, p1):
## return (p0[0]+p1[0], p0[1]+p1[1])
##
##def rot(l, e, n):
## return l[(l.index(e) + n) % len(l)]
##
##p=(0,0)
##dirs = [(1,0), (0,1), (-1,0), (0,-1)]
##d=dirs[0]
##for c in 'flfrffrffr':
##    if c == 'f':
##        p = add_p(p, d)
##     elif c == 'l':
##         d = rot(dirs, d, 1)
##     elif c == 'r':
##         d = rot(dirs, d, -1)
##     print(p)

## матрица поворота
## M(x) :=matrix([ cos(x),-sin(x)],
##               [ sin(x), cos(x)]);
##
## формула углов в радианы
## rad(x):=x*%pi/180;
##
## вектор должен быть в столбцовой форме
## vec(x,y) := matrix([x],
##                    [y]);
##
## матрица поворота на 90 градусов
## M(rad(90));
##    => matrix([0, -1],
##              [1,  0])
##
## если помножить матрицу поворота на вектор x,y то получаем вектор -y,x
## M(rad(90)) * vec(x,y);
##    => matrix([-y],
##              [ x])
##
## id. для поворота в другую сторону меняем знаки в матрице поворота и
##     получем x,y => y,-x
##def left(v):
##    x,y=v
##    return -y,x
##
##def right(v):
##    x,y=v
##    return y,-x
##
##def add_v(v0,v1):
##    return (v0[0]+v1[0],
##            v0[1]+v1[1])
##
##def turtle(coord, direction):
##    p=coord                     # позиция
##    d=(1,0)                     # направление
##    for r in range(direction):  # нам не нужна таблица, можно просто
##        d = left(d)             # повернуться нужное количество раз
##    for c in 'flfrffrffr':
##        if c == 'f':
##            p = add_v(p, d)
##        elif c == 'l':
##            d = left(d)
##        elif c == 'r':
##            d = right(d)
##        print(p)
##
##turtle((0,0),0)

##from math import radians, sin, cos
##
##def rot(v, a):
##    x,y = v
##    # зачем round? потому что во float математике иногда крадутся ошибки
##    # похорошему нужно бы сделать матан на эту формулу, но я уже заебался
##    # с этой задачей
##    return round(cos(a)*x-sin(a)*y), round(cos(a)*y+sin(a)*x)
##
##def add_v(v0,v1):
##    x0,y0 = v0
##    x1,y1 = v1
##    return x0+x1, x1+y1
##
##def turtle(coord, direction):
##    p=coord        
##    d=(1,0)
##    for r in range(direction):
##        d = rot(d, radians(90))
##    for c in 'flfrffrffr':
##        if c == 'f':
##            p = add_v(p, d)
##        elif c == 'l':
##            d = rot(d, radians(90))
##        elif c == 'r':
##            d = rot(d, radians(-90))
##        print(p)
##
##turtle((0,0),0)

##p=0
##d=0
##dirs = [1, 1j, -1, -1j]
##l=len(dirs)
##for c in 'flfrffrffr':
##    if c == 'f':
##        p += dirs[d%l]
##    elif c == 'l':
##        d += 1
##    elif c == 'r':
##        d -= 1
##    print(p)

robo = turtle((0,0),0)
start = next(robo)
for c in "flfrffrffr":
    print(*robo.send(c))
