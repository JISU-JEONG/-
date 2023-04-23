# no.7579 토마토
import sys
from collections import deque
from itertools import chain
delta = [
    (-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1)
]

M, N, H = map(int, sys.stdin.readline().split())
board = [
    [
        list(map(int, sys.stdin.readline().split()))
        for _ in range(N)
    ]
    for _ in range(H)
]

fresh_tomato_list = [
    (i, j, k)
    for i in range(N)
    for j in range(M)
    for k in range(H)
    if board[k][i][j] == 1
]


def check_valid_coordinate(x, y, z):
  if 0 <= x < N and 0 <= y < M and 0 <= z < H:
    return True
  return False


def bfs(que):
  que = deque(que)
  visit = [
      [
          [0] * M
          for _ in range(N)
      ]
      for _ in range(H)
  ]
  for x, y, z in que:
    visit[z][x][y] = 1

  while que:
    rx, ry, rz = que.popleft()
    for dx, dy, dz in delta:
      nx, ny, nz = rx + dx, ry + dy, rz + dz
      if check_valid_coordinate(nx, ny, nz) and not visit[nz][nx][ny]\
         and board[nz][nx][ny] == 0:
        visit[nz][nx][ny] = 1
        board[nz][nx][ny] = board[rz][rx][ry] + 1
        que.append((nx, ny, nz))

  flatten = list(chain.from_iterable(chain.from_iterable(board)))
  if 0 in flatten:
    return -1
  return max(flatten) - 1


result = bfs(fresh_tomato_list)

print(result)
