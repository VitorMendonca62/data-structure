class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    self.parent = None
    
  def __str__(self):
    return str(self.data)
  
class BinaryTree:
  def __init__(self, limit, data = None):
    self.root = Node(data) if data else None
    self.limit = limit
    self.repeats = []
    
  def height(self, node = None):
    if node is None:
      return 0
    
    height_left = 0
    height_right = 0
    
    if node.left:
      height_left = self.height(node.left)
    
    if node.right:
      height_right = self.height(node.right)
      
    if height_right > height_left:
      return height_right + 1
    return height_left + 1
  
  def in_order_reverse(self, node = None):
    string = ""
    if node is None:
      node = self.root
    if node.right:
      string += self.in_order_reverse(node.right)
    string += f"{node.data} "
    if node.left:
      string += self.in_order_reverse(node.left)
    return string
  
  def sum_total(self):
    string = self.in_order_reverse().split()
    soma = 0
    
    all_elemets = string + self.repeats
    
    for num in range(len(all_elemets)):
      all_elemets[num] = int(all_elemets[num]) 
    
    all_elemets.sort(reverse=True)
    for num in range(self.limit):
      if num < len(all_elemets):
        soma += all_elemets[num]

    return soma
  
  def is_in_tree(self, value, add):
    temp_node = self.root
    
    while temp_node and temp_node.data != value:
      parent = temp_node
      if value > parent.data:
        temp_node = temp_node.right
      elif value < parent.data:
        temp_node = temp_node.left
    
    if add and temp_node and temp_node.data == value:
      self.repeats.append(int(value))
      return False
    return True

  def insert(self, value):
    if self.is_in_tree(value, True):
      parent = None
      temp_node = self.root

      while temp_node:
        parent = temp_node
        if value > parent.data:
          temp_node = temp_node.right
        elif value < parent.data:
          temp_node = temp_node.left
      
      node = Node(value)
      node.parent = parent
      if parent is None:
        self.root = node
      elif value > parent.data:
        parent.right = node
      elif value < parent.data:
        parent.left = node
      
      self.balance(node)

  def rotation_right(self, node):
    if node == self.root:
      self.root = node.left 
    
    parent = node.left
    
    if parent:
      parent_parent = node.parent
      if parent and parent.right:
        node.left = parent.right
        node.left.parent = node
      else: node.left = None
      
      parent.right = node
      parent.parent = node.parent
      node.parent = parent
      
      if parent_parent: parent_parent.right = parent
        
  def rotation_left(self, node = None):
    if node == self.root:
      self.root = node.right 
    
    parent = node.right
    
    if parent:
      parent_parent = node.parent
      if parent and parent.left:
        node.right = parent.left
        node.right.parent = node
      else: node.right = None
      
      parent.left = node
      parent.parent = node.parent
      node.parent = parent
      
      if parent_parent: parent_parent.left = parent

  def double_rotation_right(self, node ):
    self.rotation_left(node)
    self.rotation_right(self.root)
    
  def double_rotation_left(self, node):
    self.rotation_right(node)
    self.rotation_left(self.root)
    
  def balance(self, node = None):
    if node is None:
      node = self.root
    height_left = self.height(self.root.left)
    height_right = self.height(self.root.right)
    
    if abs(height_left - height_right) > 1:
      parent, parent_parent = None, None
      
      if node: parent = node.parent
      if parent: parent_parent = parent.parent
      
      condition_left = (parent_parent.left == parent) and parent.left == node
      condition_right = (parent_parent.right == parent) and parent.right == node
      condition_for_simple = condition_left or condition_right
      
      if height_left > height_right:
        if condition_for_simple: self.rotation_right(self.root)
        else: self.double_rotation_right(self.root.left)
      else:
        if condition_for_simple: self.rotation_left(self.root)
        else: self.double_rotation_left(self.root.right)
      self.balance(node)

classes = input()
hogwarts_classes = input().split(" ")
cin_classes = input().split(" ")
items = hogwarts_classes + cin_classes 
hours = int(input())

tree = BinaryTree(hours)

for item in items:
  tree.insert(int(item))

print("valor total de conhecimento:", tree.sum_total())