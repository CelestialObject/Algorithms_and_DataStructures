import math
from typing import Any
from dataclasses import dataclass, field

class BinTreeNode:
  def __init__(self, item) -> None:
    self.item = item
    self.left = None
    self.right = None 
    self.parent = None

    def get_item(self):
      return self.item
    
    def set_item(self, item):
      self.item = item
      return None

    def has_left(self):
      return (self.left is not None)

    def left_child(self):
      return self.left
    
    def has_right(self):
      return (self.right is not None)
    
    def right_child(self):
      return self.right
    
    def set_right_child(self, r) -> None:
      self.right = r
      return None

    def set_left_child(self, l) -> None:
      self.left = l
      return None
    
    def del_right_child(self) -> None:
      self.right = None
      return None 

    def del_left_child(self) -> None:
      self.left = None
      return None 

    def get_parent(self):
      return self.parent

    def is_root(self):
      return (self.parent is None)
    
    def is_leaf(self):
      return (self.left is not None) and (self.right is not None)

@dataclass(slots=True)
class BinaryTree:
  root : BinTreeNode = field(default_factory=BinTreeNode)

  def traversal_order(self, x : BinTreeNode):
    res = []
    if x.is_leaf(): res.append(x)
    else:
      if x.has_left(): res.append(self.traversal_order(x.left_child()))
      res.append(x)
      if x.has_right(): res.append(self.traversal_order(x.right_child()))
    return res

  def subtree(self, x : BinTreeNode):
    pass

  def depth(self, x : BinTreeNode) -> int:
    pass

  def height(self, x : BinTreeNode) -> int:
    pass 

  def subtree_first(self, x : BinTreeNode) -> BinTreeNode:
    """ return first node in the traversal order of subtree(x)
    """
    cur_node = x
    while (cur_node.has_left()): # if x has a left child
      cur_node = cur_node.left_child()
      if cur_node.is_leaf(): return cur_node # return if left child is a leaf
    return cur_node # if subtree(x) has no left subtree, return x
  
  def subtree_last(self, x : BinTreeNode) -> BinTreeNode:
    """ return first node in the traversal order of subtree(x)
    """
    cur_node = x
    while (cur_node.has_right()): # if x has a left child
      cur_node = cur_node.right_child()
      if cur_node.is_leaf(): return cur_node # return if left child is a leaf
    return cur_node # if subtree(x) has no left subtree, return x

  def succesor(self, x : BinTreeNode) -> BinTreeNode:
    """ return succesor of Node x in traversal order of the binary tree
    """
    
    if x.has_right(): return self.subtree_first(x.right_child())
    else:
      cur_node = x
      if cur_node.is_root(): return cur_node
      p = cur_node.get_parent()
      while (p.left_child() != cur_node):
        cur_node = cur_node.get_parent()
        p = cur_node.parent()
      return p

  def predecesor(self, x : BinTreeNode) -> BinTreeNode:
    """ return predecesor of Node x in traversal order of the binary tree
    """
    if x.has_left(): return self.subtree_last(x.left_child())
    else:
      cur_node = x
      if cur_node.is_root(): return cur_node
      p = cur_node.get_parent()
      while (p.right_child() != cur_node):
        cur_node = cur_node.get_parent()
        p = cur_node.parent()
      return p

  def insert_before(self, node : BinTreeNode, x : BinTreeNode) -> None:
    if (not node.has_left()):
      node.set_left_child(x)
      return None
    else:
      p = self.predecesor(node)
      p.set_right_child(x)

  def insert_after(self, node : BinTreeNode, x : BinTreeNode) -> None:
    if (not node.has_right()):
      node.set_right_child(x)
      return None
    else:
      s = self.succesor(node)
      s.set_left_child(x)
      return None
  
  def swap_items(self, x : BinTreeNode, y : BinTreeNode) -> None:
    x_item = x.get_item()
    y_item = y.get_item()
    x.set_item(y_item)
    y.set_item(x_item)
    return None 

  def delete_node(self, x : BinTreeNode) -> None:
    if x.is_leaf():
      p = x.get_parent()
      p.del_left_child()
    else:
      if x.has_left():
        pr = self.predecesor(x)
        self.swap_items(x, pr)
        self.delete_node(pr)
      if x.has_right():
        s = self.succesor(x)
        self.swap_items(x, s)
        self.delete_node(s)

  def __repr__(self) -> str:
    traversal_order = self.traversal_order(self.root)
    res = ""
    for node in traversal_order:
      res += f'{node.get_item()}, '
    return res