# no.27433 팩토리얼2
import sys

N = int(sys.stdin.readline())
dp = [1, 1] + [0] * (N - 1)


def factorial(n):
  if dp[n] > 0:
    return dp[n]
  dp[n] = n * factorial(n - 1)
  return dp[n]


print(factorial(N))
