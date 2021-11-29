# Longest Increasing Subsequence (LIS)
# Given a string A, find a longest (not necessarily contiguous)
# subsequence of A that strictly increases (lexicographically).
# Example: A = carbohydrate
# solution: abort, of length 5
# Maximization problem on length of subsequence
def generate_lis(p, A, m):
  s = A[m]
  parent = p[m]
  while (parent is not None):
    s += A[parent]
    parent = p[parent]
  return s

def lis(A):
  n = len(A)
  L = [1] * n
  p = [None] * n

  # L[i] : max len of increasing sub-sequence in A[i:] including A[i]
  for i in range(n-2, -1, -1): # so A[i+1] exists
    for j in range(i+1, n): # n-1 >= j > i
      if A[j] > A[i]:
        cur = max(L[i], 1+L[j])
        if cur > L[i]:
          L[i] = cur
          p[i] = j
  max_lis = max(L)
  return max_lis, generate_lis(p, A, L.index(max_lis))