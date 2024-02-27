class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
  
class BinaryTree:
  def __init__(self, data = None):
    self.root = Node(data) if data else None
    
  def in_order(self, node = None):
    string = ""
    if node is None:
      node = self.root
    if node.left:
      string += self.in_order(node.left)
    string += f"{node.data} "
    if node.right:
      string += self.in_order(node.right)
    return string
      
  def insert(self, value):
    parent = None
    temp_node = self.root

    while temp_node:
      parent = temp_node
      if value > parent.data:
        temp_node = temp_node.right
      elif value < parent.data:
        temp_node = temp_node.left
    
    node = Node(value)
    if parent is None:
      self.root = node
    elif value > parent.data:
      parent.right = node
    elif value < parent.data:
      parent.left = node
      
items = input().split(" ")

tree = BinaryTree()
for item in items:
  tree.insert(int(item))

print("".join(tree.in_order()[:-1]))
