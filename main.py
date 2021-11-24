# Copyright 2021, Aman Gupta
from DataStructures.BinaryHeaps.binary_heap import BinaryHeap

def main():
  # A = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
  # bh = BinaryHeap(A, max_heap=False)
  # print(bh, bh.length, bh.heap_size)
  # print(bh.extract_heap_min())
  # print(bh, bh.length, bh.heap_size)

  A = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
  bh = BinaryHeap(A, max_heap=False)
  print(bh, bh.length, bh.heap_size)
  bh.decrease_key(5, 0)
  print(bh, bh.length, bh.heap_size)
if __name__=='__main__':
  main()