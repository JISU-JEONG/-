# no.2583 영역 구하기
import sys


delta = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

M, N, K = map(int, sys.stdin.readline().split())
board = [
    [0] * M
    for _ in range(N)
]

for _ in range(K):
  x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
  for i in range(x1, x2):
    for j in range(y1, y2):
      board[i][j] = 1


def check_valid_coordinate(x, y):
  if 0 <= x < N and 0 <= y < M:
    return True
  return False


def bfs(x, y):
  visit[x][y] = 1
  que = [(x, y)]
  cnt = 1
  while que:
    rx, ry = que.pop(0)
    for dx, dy in delta:
      nx, ny = rx + dx, ry + dy
      if check_valid_coordinate(nx, ny) and not visit[nx][ny]\
         and not board[nx][ny]:
        visit[nx][ny] = 1
        que.append((nx, ny))
        cnt += 1
  return cnt


visit = [
    [0] * M
    for _ in range(N)
]
result = []
for i in range(N):
  for j in range(M):
    if not visit[i][j] and not board[i][j]:
      result.append(bfs(i, j))

print(len(result))
print(*sorted(result))
