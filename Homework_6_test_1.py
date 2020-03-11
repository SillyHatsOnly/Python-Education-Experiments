'''
Вводятся строки, содержащие четыре целых числа и символ, разделённые пробелами. Код символа:
32 < c < 128. Это абсцисса, ордината (ось ординат направлена вниз) некоторых точек, а также
длина и ширина построенных на них прямоугольников, «нарисованных» с помощью указанных
символов. Последняя строка начинается на четыре нуля. Вывести наименьшую область, содержащюю
все раскрашенные точки, нарисованные в порядке ввода прямоугольников. Область также
прямоугольна и изначально заполнена символами '.'. Координаты и размеры могут быть
отрицательны (в этом случае прямогуольник откладывается от исходной точки в противоположную
сторону, а сама точка в него не попадает) или равны нулю.

Пример:
Input:
1 2 10 10 *
-2 -1 10 10 #
3 4 -10 10 @
5 6 10 -10 %
0 0 0 0 0
Output:
............%%%%%%%%%%
............%%%%%%%%%%
............%%%%%%%%%%
.....#######%%%%%%%%%%
.....#######%%%%%%%%%%
.....#######%%%%%%%%%%
.....#######%%%%%%%%%%
.....#######%%%%%%%%%%
@@@@@@@@@@##%%%%%%%%%%
@@@@@@@@@@##%%%%%%%%%%
@@@@@@@@@@#####***....
@@@@@@@@@@#####***....
@@@@@@@@@@#####***....
@@@@@@@@@@********....
@@@@@@@@@@********....
@@@@@@@@@@********....
@@@@@@@@@@............
@@@@@@@@@@............
'''

def trim_image():
    square_arr = []
    # запускаем цикл ввода параметров
    while True:
        x,y,a,b,symbol = str(input()).split(' ')
        x,y,a,b = int(x), int(y), int(a), int(b)
        if ord(symbol) < 32 or ord(symbol) > 128:
            return print('Symbol error!')
        if x == 0 and y == 0 and a == 0 and b == 0:
            break
        else:
            square_arr.append([x,y,a,b,symbol])
    # найдём минимальные координаты по x и по y:
    min_x, min_y = None, None
    new_square_arr = []
    for x, y, a, b, symbol in square_arr:
        if a < 0:
            x = x + a
            a = abs(a)
        if b < 0:
            y = y + b
            b = abs(b)
        if min_x == None or min_x > x:
            min_x = x
        if min_y == None or min_y > y:
            min_y = y
        new_square_arr.append([x,y,a,b,symbol])
    # переопределим диапазон значений:
    max_x, max_y = None, None
    square_arr = []
    for x, y, a, b, symbol in new_square_arr:
        x = x + abs(min_x)
        y = y + abs(min_y)
        if max_x == None or max_x < x+a:
            max_x = x+a
        if max_y == None or max_y < y+b:
            max_y = y+b
        square_arr.append([x,y,a,b,symbol])
    # Заполняем поле
    answer_arr = [['.' for x in range(0,max_x)] for y in range(0, max_y)]
    for x, y, a, b, symbol in square_arr:
        for h in range(y, y+b):
            for w in range(x, x+a):
                answer_arr[h][w] = symbol
    for y in range(0, max_y):
        for x in range(0, max_x):
            print(answer_arr[y][x], end='')
        print()
    
trim_image()
