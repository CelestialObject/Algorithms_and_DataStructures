# Bowling
# - Given n pins labeled 0, 1, . . . , n � 1
# - Pin i has value vi
# - Ball of size similar to pin can hit either
# -- 1 pin i, in which case we get vi points
# -- 2 adjacent pins i and i + 1, in which case we get vi · vi+1 points
# - Once a pin is hit, it can’t be hit again (removed)
# - Problem: Throw zero or more balls to maximize total points
# - Example: [ -1, !1! , !1! , !1! , !9, 9! , !3! , !-3, -5! , !2, 2! ]
def bowling(v):
  n =  len(v)
  B = {}
  hit_strat = [0]*n
  
  # Bottom up iterative dynamic programming 
  B[n+1] = 0
  B[n] = 0
  for i in range(n-1, -1, -1):
    B_no_hit = B[i+1]
    B_one_hit = v[i] + B[i+1]
    B_two_hit = v[i]*v[i+1] + B[i+2] if (i+1 < n) else 0
    Bi = [B_no_hit, B_one_hit, B_two_hit]
    Bi_max = max(Bi)
    B[i], hit_strat[i] = Bi_max, Bi.index(Bi_max)
  # clean hit strat: dont hit (i+1) if hit_strat[i] = 2 -> (i, i+1) hit together
  for i in range(n-1):
    if (hit_strat[i] == 2): hit_strat[i+1] = 0
  return B[0], hit_strat
