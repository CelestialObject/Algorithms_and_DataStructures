# Using dynamic programming (bottom-up iterative solution (slightly better))
def fib(n):
  F = {}
  F[0], F[1] = 0, 1
  for i in range(2, n+1):
    F[i] = F[i-1] + F[i-2]
  return F[n]
