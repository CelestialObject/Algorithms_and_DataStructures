from .binary_tree import BinaryTree, BinaryTreeNode

class BSTNode(BinaryTreeNode):
  def subtree_find(N, k):
    item_key = N.item.key
    if (k < item_key):
      if (N.left): return N.left.subtree_find(k)
    elif (k > item_key):
      if (N.right): return N.right.subtree_find(k)
    else:
      return N
    return None

  def subtree_find_next(N, k):
    if (N.item.key <= k):
      if (N.right): return N.right.subtree_find_next(k)
      else: return None
    elif (N.left):
      M = N.left.subtree_find_next(k)
      if M: return M
    return N

  def subtree_find_prev(N, k):
    if (N.item.key >= k):
      if (N.left): return N.left.subtree_fin_prev(k)
      else: return None
    elif (N.right):
      M = N.right.subtree_find_prev(k)
      if M: return M
    return N
    
  def subtree_insert(N, M) -> None:
    if (M.item.key < N.item.key):
      if (N.left): N.left.subtree_insert(M)
      else: N.subtree_insert_before(M)
    elif (M.item.key > N.item.key):
      if (N.right): N.right.subtree_insert(M)
      else: N.subtree_insert_after(M)
    else: N.item = M.item
    return None

class BST(BinaryTree):
  def __init__(self) -> None:
    super().__init__(NodeType=BSTNode)
  
  def insert(self, x):
    new_node = self.NodeType(x)
    if (self.root):
      self.root.subtree_insert(new_node)
      if new_node.parent is None: return False
    else:
      self.root = new_node
    self.size += 1
    return True
  
  def delete(self, k):
    assert self.root
    node = self.root.subtree_find(k)
    assert node
    ext = node.subtree_delete()
    if (ext.parent is None): self.root = None
    self.size -= 1
    return ext.item

  def build_set(self, X):
    for x in X: self.insert(x)
    return None
  
  def find_min(self):
    if (self.root): return self.root.subtree_first().item
  
  def find_max(self): 
    if (self.root): return self.root.subtree_last().item
  
  def find(self, k):
    if (self.root):
      node = self.root.subtree_find(k)
      if (node): return node.item
  
  def find_next(self, k):
    if (self.root):
      node = self.root.subtree_find_next(k)
      if (node): return node.item
  
  def find_prev(self, k):
    if (self.root):
      node = self.root.subtree_find_prev(k)
      if (node): return node.item
  