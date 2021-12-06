from typing import Any

class BinaryTreeNode:
  def __init__(N, x : Any) -> None:
    N.item = x
    N.left = None
    N.right = None
    N.parent = None
  
  def traversal_order(N):
    if (N.left): yield from N.left.traversal_order()
    yield N
    if (N.right): yield from N.right.traversal_order()
  
  def subtree_first(N): # O(h): return leftmost leaf in subtree(current_node)
    if (N.left): return N.left.subtree_first()
    else: return N
  
  def subtree_last(N): # O(h): return rightmost leaf in subtree(current_node)
    if (N.right): return N.right.subtree_last()
    else: return N

  def successor(N):
    if (N.right): return N.right.subtree_first()
    while ((N.parent) and (N is N.parent.right)): N = N.parent
    return N.parent
  
  def predecessor(N):
    if (N.left): return N.left.subtree_last()
    while ((N.parent) and (N is N.parent.left)): N = N.parent
    return N.parent
  
  def insert_subtree_before(N, M) -> None:
    if N.left:
      N = N.left.subtree_last()
      N.right, M.parent = M, N
    else:
      N.left, M.parent = M, N
  
  def insert_subtree_after(N, M) -> None:
    if N.right:
      N = N.right.subtree_first()
      N.left, M.parent = M, N
    else:
      N.right, M.parent = M, N
  
  def subtree_delete(N):
    if (N.left or N.right):
      if (N.left): M = N.predecessor()
      else: M = N.successor()
      N.item, M.item = M.item, N.item
      return M.subtree_delete()    
    if N.parent:
      if (N is N.parent.left): N.parent.left = None
      else: N.parent.right = None
    return N

class BinaryTree:
  def __init__(T, NodeType=BinaryTreeNode) -> None:
    T.root = None
    T.size = 0
    T.NodeType = NodeType

  def __len__(T): return T.size

  def __iter__(T):
    if (T.root):
      for N in T.root.subtree_iter():
        yield N.item
  
  def build(T, A):
    N = [ai for ai in A]
    def build_subtree(N, i, j):
      c = (i+j)//2
      root = T.NodeType(N[c])
      if (i < c): root.left, root.left.parent = build_subtree(A, i, c-1), root

