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
