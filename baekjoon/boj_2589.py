# no.2589 보물섬
import sys
from collections import deque
from itertools import chain


delta = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

N, M = map(int, sys.stdin.readline().split())
board = [
    sys.stdin.readline().strip()
    for _ in range(N)
]


def check_valid_coordinate(x, y):
  if 0 <= x < N and 0 <= y < M:
    return True
  return False


def bfs(x, y):
  que = deque([(x, y)])
  visit = [
      [0] * M
      for _ in range(N)
  ]
  visit[x][y] = 1
  while que:
    rx, ry = que.popleft()
    for dx, dy in delta:
      nx, ny = rx + dx, ry + dy
      if check_valid_coordinate(nx, ny) and not visit[nx][ny]\
         and board[nx][ny] == "L":
        visit[nx][ny] = 1 + visit[rx][ry]
        que.append((nx, ny))
  return max(list(chain.from_iterable(visit))) - 1


result = []

for i in range(N):
  for j in range(M):
    if board[i][j] == "L":
      result.append(bfs(i, j))

print(max(result))
