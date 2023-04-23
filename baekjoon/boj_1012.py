# no.1012 유기농 배추
import sys


delta = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

T = int(sys.stdin.readline())
for _ in range(T):
  M, N, L = map(int, sys.stdin.readline().split())
  board = [
      [0] * M
      for _ in range(N)
  ]

  for _ in range(L):
    y, x = map(int, sys.stdin.readline().split())
    board[x][y] = 1

  def check_valid_coordinate(x, y):
    if 0 <= x < N and 0 <= y < M:
      return True
    return False

  def bfs(x, y):
    visit[x][y] = 1
    que = [(x, y)]

    while que:
      rx, ry = que.pop(0)
      for dx, dy in delta:
        nx, ny = rx + dx, ry + dy
        if check_valid_coordinate(nx, ny) and not visit[nx][ny]\
           and board[nx][ny]:
          visit[nx][ny] = 1
          que.append((nx, ny))

  cnt = 0
  visit = [
      [0] * M
      for _ in range(N)
  ]
  for i in range(N):
    for j in range(M):
      if not visit[i][j] and board[i][j]:
        bfs(i, j)
        cnt += 1
  print(cnt)
