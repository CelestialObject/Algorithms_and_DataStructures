import math
from dataclasses import dataclass, field

@dataclass(slots=True)
class BinaryHeap:
  A : list = field(default_factory=list)
  max_heap : bool = True
  heap_size : int = field(init=False, default=0)
  length : int = field(init=False, default=0)

  def __post_init__(self) -> None:
    self.length = len(self.A)
    self.build_heap()

  def __repr__(self) -> str:
    return str(self.A[0:self.heap_size])

  def parent(self, i: int) -> int:
    return math.floor((i-1)/2) if (i > 0) else 0
  
  def left(self, i: int) -> int:
    return (2*i) + 1

  def right(self, i: int) -> int:
    return (2*i) + 2
  
  def max_heapify(self, i: int) -> None: # O(lg n)
    l = self.left(i)
    r = self.right(i)
    is_valid_l = (l <= self.heap_size-1)
    is_valid_r = (r <= self.heap_size-1)
    max_idx = l if ((is_valid_l) and (self.A[l] > self.A[i])) else i
    max_idx = r if ((is_valid_r) and (self.A[r] > self.A[max_idx])) else max_idx
    if (max_idx != i):
      self.A[i], self.A[max_idx] = self.A[max_idx], self.A[i]
      self.max_heapify(max_idx)
    return None

  def min_heapify(self, i: int) -> None:
    l = self.left(i)
    r = self.right(i)
    is_valid_l = (l <= self.heap_size-1)
    is_valid_r = (r <= self.heap_size-1)
    min_idx = l if ((is_valid_l) and (self.A[l] < self.A[i])) else i
    min_idx = r if ((is_valid_r) and (self.A[r] < self.A[min_idx])) else min_idx
    if (min_idx != i):
      self.A[i], self.A[min_idx] = self.A[min_idx], self.A[i]
      self.min_heapify(min_idx)
    return None
  
  def heapify(self, i: int) -> None:
    if (self.max_heap): self.max_heapify(i)
    else: self.min_heapify(i)
    return None

  def build_heap(self) -> None:
    self.heap_size = self.length
    for i in range(math.floor((self.length-1)/2), -1, -1): self.heapify(i)
    return None
  
  def heap_sort(self) -> list:
    if (not self.max_heap): # if saved as a min heap, then remake a max heap
      self.max_heap = True
      self.build_heap()
    # sorting done in-place! so may need to rebuild the heap after heap_sort
    for i in range(self.length-1, 0, -1): # O(n.log(n))
      self.A[0], self.A[i] = self.A[i], self.A[0]
      self.heap_size -= 1
      self.max_heapify(0)
    return self.A
  
  # Functions to implement Priority queue
  def heap_max(self):
    if (not self.heap_max):
      print('heap not saved as a max_heap. rebuild max heap')
      return None
    return self.A[0]
  
  def heap_min(self):
    if (self.max_heap):
      print('heap not saved as a min_heap. rebuild min heap')
      return None
    return self.A[0]

  def extract_heap_max(self):
    if (not self.max_heap):
      print('heap not saved as a max_heap. rebuild max heap')
      return None
    heap_max = self.heap_max()
    self.A[0] = self.A[self.heap_size-1]
    self.heap_size -= 1
    self.max_heapify(0)
    return heap_max
  
  def extract_heap_min(self):
    if (self.max_heap):
      print('heap not saved as a min_heap. rebuild min heap')
      return None
    heap_min = self.heap_min()
    self.A[0] = self.A[self.heap_size-1]
    self.heap_size -= 1
    self.min_heapify(0)
    return heap_min
  
  def increase_key(self, i, key):
    if (not self.max_heap):
      print('heap not saved as a max_heap. rebuild max heap')
      return None
    if (key < self.A[i]):
      print("new key is smaller than current key")
      return None 
    self.A[i] = key
    while((i > 0) and (self.A[self.parent(i)] < self.A[i])):
      self.A[i], self.A[self.parent(i)] = self.A[self.parent(i)], self.A[i]
      i = self.parent(i)
    return None

  def decrease_key(self, i, key):
    if (self.max_heap):
      print('heap not saved as a min_heap. rebuild min heap')
      return None
    if (key > self.A[i]):
      print("new key is larger than current key")
      return None 
    self.A[i] = key
    while((i > 0) and (self.A[self.parent(i)] > self.A[i])):
      self.A[i], self.A[self.parent(i)] = self.A[self.parent(i)], self.A[i]
      i = self.parent(i)
    return None
  
  def maxheap_insert(self, key):
    if (not self.max_heap):
      print("not a max heap")
      return None
    self.A.append(float('-inf'))
    self.heap_size += 1
    self.length +=1
    self.increase_key(self.heap_size-1, key)
  
  def minheap_insert(self, key):
    if (self.max_heap): return None
    self.A.append(float('inf'))
    self.heap_size += 1
    self.length += 1
    self.decrease_key(self.heap_size-1, key)
  