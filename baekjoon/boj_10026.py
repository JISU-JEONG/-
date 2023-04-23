# no.10026 적록색약
import sys


delta = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

N = int(sys.stdin.readline())

board = [
    sys.stdin.readline()
    for _ in range(N)
]


def check_valid_coordinate(x, y):
  if 0 <= x < N and 0 <= y < N:
    return True
  return False


def check_valid_point(x, y, o_color, t_color, weekness):
  if weekness:
    if o_color == t_color:
      return True
    if o_color + t_color in "RGR":
      return True
  else:
    if o_color == t_color:
      return True
  return False


def bfs(x, y, weekness):
  visit[x][y] = 1
  que = [(x, y)]

  while que:
    rx, ry = que.pop(0)
    for dx, dy in delta:
      nx, ny = rx + dx, ry + dy
      if not check_valid_coordinate(nx, ny):
        continue
      if check_valid_point(nx, ny, board[x][y], board[nx][ny], weekness)\
         and not visit[nx][ny]:
        visit[nx][ny] = 1
        que.append((nx, ny))


result = []
for weekness in (False, True):
  cnt = 0
  visit = [
      [0] * N
      for _ in range(N)
  ]
  for i in range(N):
    for j in range(N):
      if not visit[i][j]:
        bfs(i, j, weekness)
        cnt += 1
  result.append(cnt)

print(f"{result[0]} {result[1]}")
