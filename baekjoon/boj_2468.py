# no.2468 안전 영역
import sys
from collections import deque
from itertools import chain

delta = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

N = int(sys.stdin.readline())
board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(N)
]
flatten = list(chain.from_iterable(board))
max_h = max(flatten)
min_h = min(flatten)

print(max_h, min_h)


def check_valid_coordinate(x, y):
  if 0 <= x < N and 0 <= y < N:
    return True
  return False


def bfs(x, y, k):
  que = deque([(x, y)])
  visit[x][y] = 1

  while que:
    rx, ry = que.popleft()
    for dx, dy in delta:
      nx, ny = rx + dx, ry + dy
      if check_valid_coordinate(nx, ny) and not visit[nx][ny]\
         and board[nx][ny] > k:
        visit[nx][ny] = 1
        que.append((nx, ny))


result = []
for h in range(max(min_h - 1, 1), max_h + 1):
  visit = [
      [0] * N
      for _ in range(N)
  ]
  cnt = 0
  for i in range(N):
    for j in range(N):
      if not visit[i][j] and board[i][j] > h:
        bfs(i, j, h)
        cnt += 1
  result.append(cnt)
print(max(result))
