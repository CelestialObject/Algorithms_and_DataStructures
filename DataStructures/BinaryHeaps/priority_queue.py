from dataclasses import dataclass
from .binary_heap import BinaryHeap

@dataclass(slots=True)
class PriorityQueue(BinaryHeap):
  max_prio : bool = True
  