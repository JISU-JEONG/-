# no.2606 바이러스
import sys


delta = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

N = int(sys.stdin.readline())
visit = [
    [0] * N
    for _ in range(N)
]

board = [
    sys.stdin.readline()
    for _ in range(N)
]


def check_valid_coordinate(x, y):
  if 0 <= x < N and 0 <= y < N:
    return True
  return False


def check_valid_point(x, y):
  if check_valid_coordinate(x, y) and board[x][y] == "1":
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
      if check_valid_point(nx, ny) and not visit[nx][ny]:
        visit[nx][ny] = 1
        cnt += 1
        que.append((nx, ny))
  return cnt


result_list = []
for i in range(N):
  for j in range(N):
    if not visit[i][j] and board[i][j] == "1":
      result_list.append(bfs(i, j))

result_list.sort()
total = len(result_list)
print("\n".join(map(str, [total] + result_list)))
