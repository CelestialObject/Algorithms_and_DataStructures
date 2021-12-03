def select(A, j, k=5):
  n = len(A)
  med_Ak = [0] * (n//k + 1)
  for t, i in enumerate(range(0, n, k)):
    Ak = A[i : i+k] if (i + k < n) else A[i:]
    med_Ak[t] = sorted(Ak)[2] if (len(Ak) == 5) else sorted(Ak)[len(Ak)//2]
  
  