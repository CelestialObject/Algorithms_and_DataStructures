# longest palindromic subsequence
def construct_lps(s, p):
  pass

def lps(s):
  n = len(s)
  L = [[1]*n for _ in range(n)]
  p = {i : None for i in range(n)}

  for i in range(n-1, -1, -1):
    for j in range(i+1, n):
      if (s[i] == s[j]):
        p[j] = i
        p[i] = j
        if (i+1 == j): L[i][j] = 2
        else: L[i][j] = 2 + L[i+1][j-1]
      else: L[i][j] = max(L[i+1][j], L[i][j-1])
  print(p)
  return L[0][n-1]