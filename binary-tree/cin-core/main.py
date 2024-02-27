class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    self.parent = None
    
  def __str__(self):
    return str(self.data)
  
class BinaryTree:
  def __init__(self, data = None):
    self.root = Node(data) if data else None

  def is_in_tree(self, value):
    temp_node = self.root
    count = 0
    while temp_node and temp_node.data != value:
      count += 1
      parent = temp_node
      if value > parent.data:
        temp_node = temp_node.right
      elif value < parent.data:
        temp_node = temp_node.left
    
    if temp_node and temp_node.data == value:
      return count, temp_node
    else: return -1, None
      
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
    node.parent = parent
    if parent is None:
      self.root = node
    elif value > parent.data:
      parent.right = node
    elif value < parent.data:
      parent.left = node
    
    count, temp_node = self.is_in_tree(node.data)
    return count

  def rotation_right(self, node):
    if node.parent == self.root:
      self.root = node
    
    parent = node.parent
    
    if parent:
      parent_parent = parent.parent
      if node.right:
        parent.left = node.right
        parent.left.parent = parent
      else:
        parent.left = None
      
      node.right = parent
      parent.parent = node
      node.parent = parent_parent
      
      if parent_parent:
        if parent_parent.left == parent: parent_parent.left = node
        elif parent_parent.right == parent: parent_parent.right = node
        
  def rotation_left(self, node = None):
    if node.parent == self.root:
      self.root = node
    
    parent = node.parent
    
    if parent:
      parent_parent = parent.parent
      if node.left:
        parent.right = node.left
        parent.right.parent = parent
      else:
        parent.right = None
      
      node.left = parent
      parent.parent = node
      node.parent = parent_parent
      
      if parent_parent:
        if parent_parent.left == parent: parent_parent.left = node
        elif parent_parent.right == parent: parent_parent.right = node
      

  def double_rotation_right(self,node):
    self.rotation_left(node)
    self.rotation_right(node)
    
  def double_rotation_left(self, node):
    self.rotation_right(node)
    self.rotation_left(node)
    
  def send_to_top(self,node):
    while self.root != node:
      parent = node.parent
      parent_parent = parent.parent
      if parent_parent:
        if parent_parent.left == parent and parent.left == node:
          self.rotation_right(node)
        elif parent_parent.right == parent and parent.right == node:
          self.rotation_left(node)
        elif parent_parent.left == parent and parent.right == node:
          self.double_rotation_right(node)
        elif parent_parent.right == parent and parent.left == node:
          self.double_rotation_left(node)
      else: 
        if parent.left == node:
          self.rotation_right(node)
        elif parent.right == node:
          self.rotation_left(node)
          
        
  def search(self, value):
    count, node = self.is_in_tree(value)
    
    if count > -1:
      self.send_to_top(node)
    return count

tree = BinaryTree()
instruction = "."

try:
  while instruction != "":
    instruction = input()
  
    if instruction != "":
      instruction = instruction.split(" ")
      if instruction[0] == "ADD":
        count =  tree.insert(int(instruction[1]))
        print(count)
      elif instruction[0] == "SCH":
        search = tree.search(int(instruction[1]))
        print(search)
except:
  pass