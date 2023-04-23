# no.2606 바이러스
import sys

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())
edge_dict = {
    i + 1: []
    for i in range(V)
}

for i in range(E):
  N, M = map(int, sys.stdin.readline().split())
  edge_dict[N].append(M)
  edge_dict[M].append(N)


def bfs():
  visit = [0] * V
  visit[0] = 1
  que = [1]

  while que:
    n = que.pop(0)
    for e in edge_dict[n]:
      if not visit[e - 1]:
        visit[e - 1] = 1
        que.append(e)
  return sum(visit) - 1


print(bfs())
