# no.7579 토마토
import sys
from collections import deque

delta = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

M, N = map(int, sys.stdin.readline().split())
board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(N)
]

fresh_tomato_list = [
    (i, j)
    for i in range(N)
    for j in range(M)
    if board[i][j] == 1
]


def check_valid_coordinate(x, y):
  if 0 <= x < N and 0 <= y < M:
    return True
  return False


def bfs(que):
  que = deque(que)
  visit = [
      [0] * M
      for _ in range(N)
  ]
  for x, y in que:
    visit[x][y] = 1

  while que:
    rx, ry = que.popleft()
    for dx, dy in delta:
      nx, ny = rx + dx, ry + dy
      if check_valid_coordinate(nx, ny) and not visit[nx][ny]\
         and board[nx][ny] == 0:
        visit[nx][ny] = 1
        board[nx][ny] = board[rx][ry] + 1
        que.append((nx, ny))

  return max(map(max, board)) - 1


result = bfs(fresh_tomato_list)

if any(
    0 in b
    for b in board
):
  result = -1

print(result)
