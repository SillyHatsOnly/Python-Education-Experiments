'''
Ввести целые M и N, вывести последовательность 0 1 2 3 4 5 6 7 8 9 0 1 2 3 … в
виде спирально (по часовой стрелке, из верхнего левого угла) заполненной таблицы
N×M (N строк, M столбцов). Не забываем про то, что M и N могут быть чётными,
нечётными и неизвестно, какое больше.

Пример:
Input: 6,5
Output:
0 1 2 3 4 5
7 8 9 0 1 6
6 7 8 9 2 7
5 6 5 4 3 8
4 3 2 1 0 9
'''

n = int(input())
m = int(input())
mat = [[None for x in range(n)] for y in range(m)]
pos = (0,0)
moves = [(1,0),(0,1),(-1,0),(0,-1)]
movei = 0
i = 0
passed = 0
while True:
 x,y = pos
 mat[y][x] = i
 xd, yd = moves[movei]
 tpos = x, y = (x + xd, y + yd)
 if x >= 0 and y >= 0 and x < n and y < m and mat[y][x] is None:
  i += 1
  if i > 9:
      i=0
  passed = 0
  pos = tpos
 else:
  passed += 1
  movei += 1
  if passed >= len(moves):
      break
  if movei >= len(moves):
      movei = 0
for n in mat:
 print(*n)
