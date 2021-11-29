# Longest Common Subsequence (LCS)
# Given strings A and B, find a longest (not necessarily contiguous)
# subsequence of A that is also a subsequence of B.
# Example: A = hieroglyphology, B = michaelangelo
# Solution: hello or heglo or iello or ieglo, all length 5
# Maximization problem on length of subsequence
import numpy as np
def generate_lcs(p, A, B):
  # select parents with True along the parent pointer path
  s = ''
  parent = p[0][0]
  while (parent is not None):
    i, j, is_validp = parent[0], parent[1], parent[2]
    if (is_validp):
      if (A[i-1] == B[j-1]): s += A[i-1]
    parent = p[i][j]
  return s

def lcs(A, B):
  a, b = len(A), len(B)
  L = [[0]*(b+1) for _ in range(a+1)]
  p = [[None]*(b+1) for _ in range(a+1)]
  
  # Dynamic program bottom up iterative solution
  # sub-problem: L[i][j] max len of common subsequence in suffixes A[i:], B[j:]
  for i in range(a-1, -1, -1):
    for j in range(b-1, -1, -1):
      L_AiBj = 1 + L[i+1][j+1] # if A[i] = B[j], add 1 to lcs
      L_Ai = L[i+1][j] # not selecting A[i] in lcs
      L_Bj = L[i][j+1] # not selecting b[j] in lcs
      if (A[i] == B[j]):
        L[i][j] = L_AiBj
        p[i][j] = (i+1, j+1, True)
      else:
        # choices = [L_Ai, L_Bj]
        # decision = np.argmax(choices)
        # L[i][j] = choices[decision]
        L[i][j] = L_Ai if L_Ai >= L_Bj else L_Bj
        decision = 0 if L_Ai >= L_Bj else 1
        if (decision == 0): p[i][j] = (i+1, j, False)
        elif (decision == 1): p[i][j] = (i, j+1, False)
  return L[0][0], generate_lcs(p, A, B)
