# Copyright 2021, Aman Gupta
from DataStructures.BinaryTrees.binary_tree import BinaryTree, BinTreeNode

def main():
  bt = BinaryTree()
  root = BinTreeNode(3)
  A = BinTreeNode(3)
  B = BinTreeNode(1)
  C = BinTreeNode(4)
  D = BinTreeNode(2)
  E = BinTreeNode(5)
  bt.insert_root(root)
  bt.insert_after(root, A)
  bt.insert_after(root, B)
  bt.insert_after(A, C)
  bt.insert_before(C, D)
  bt.insert_before(root, E)
  bt.insert_after(E, A)
  print(bt.traversal_order(A))

if __name__=='__main__':
  main()