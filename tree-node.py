from typing import Generic, Iterator, TypeVar
"""
Tree
"""

NodeType = TypeVar('NodeType')

class Node(Generic[NodeType]):
  def __init__(self, data : NodeType):
    self.left = None
    self.right = None
    self.data = data

  def __str__(self):
    return f'({self.data} : left={self.left} right={self.right})'

  def __iter__(self):
    return in_order_traversal(self)

"""
def in_order_traversal(node : Node[NodeType]) -> Iterator[NodeType]:
  if node is None:
    return
  for v in in_order_traversal(node.left):
    yield v
  yield node
  for v in in_order_traversal(node.right):
    yield v
"""
def in_order_traversal(node : Node[NodeType]) -> Iterator[NodeType]:
  if node is None:
    return
  yield from in_order_traversal(node.left)
  yield node
  yield from in_order_traversal(node.right)

def main():
  print("Hello World")

  n = Node(10)
  n.left = Node(5)
  n.right = Node(12)

  n.left.left = Node(2)
  n.right.left = Node(11)
  print(n)

  for v in n:
    print(v.data)

if __name__ == '__main__':
  main()
