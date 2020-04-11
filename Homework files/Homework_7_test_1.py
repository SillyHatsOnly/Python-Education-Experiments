'''
Вводится карта проходимых в обе стороны тоннелей подземлья в виде строк, содержащих
разделённые пробелом названия двух пещер, которые соединяет соответствующий тоннель.
Две последние строки не содержат пробелов — это название входа в подземелье и название
выхода. Вывести "YES", если из входа можно попасть в выход, и "NO" в противном случае.
Пары могут повторяться или содержать одинаковые слова.

Пример:
Input:
guinea gauge
guinea gauge
honor mpeg
jumping guinea
markers jumping
markers jumping
markers guinea
markers gauge
markers gauge
mpeg honor
pre honor
pre mpeg
skiing mpeg
skiing solar
skiing pre
solar jackson
skiing
jumping

Otput:
NO
'''
def cave_graf():
    cave_dict = {}
    while True:
        # проверяем полученное значение
        val = str(input())
        input_values = val.split(' ')
        # если введено 1 слово, то это вход, а следом за ним указывается выход
        if len(input_values) == 1:
            main_enter = val
            main_exit = str(input())
            break
        # если введено 2 слова, то это названия связанных пещер
        enter, exit = input_values
        cave_dict.setdefault(enter, set()).add(exit)
        cave_dict.setdefault(exit, set()).add(enter)
    # создаём множество пещер, связанных с указанным в условии входом
    cave_set = set([main_enter])
    while True:
        cave_len = len(cave_set)
        # до тех пор, пока возможно, расширяем множество всеми связанными со ВХОДОМ
        # пещерами
        for i in list(cave_set):
            cave_set.update(cave_dict[i])
        # Если множество перестало увеличиваться - останавливаем цикл
        if cave_len == len(cave_set):
            break
    print('YES' if main_exit in cave_set else 'NO')
    
cave_graf()
