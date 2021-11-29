# Copyright 2021, Aman Gupta
from Algorithms.Strings.lcs import lcs
from Algorithms.Strings.lis import lis

def main():
  s = "carbohydrates"
  a = 'michaelangelo'
  b = 'hieroglyphology'
  print(lcs(a, b))
  print(len(s), lis(s))
if __name__=='__main__':
  main()