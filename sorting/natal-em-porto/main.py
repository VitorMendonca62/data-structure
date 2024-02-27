def show_playgrounds(data):
  node = data.head
  
  while node:
    string = f"{node.data}:"
    child = node.childs.head
    
    while child:
      string += f" {child.data}"
      child = child.right
    
    print(string)
    node = node.right

def bubble_sort(data):
  size = data.size
  
  def sort(node, right):
    if node == data.head:
      data.head = right
      right.left = None
      
    elif right == data.last:
      data.last = node
      
    if node.left:
      node.left.right = right
      right.left = node.left
      
    if right.right:
      right.right.left = node  
    
    node.right = right.right
    right.right = node
    node.left = right
  
  if size > 1:
    for i in range(size):
      node = data.head
      for _ in range(0, size - i - 1): 
        right = node.right
        
        if node.is_playground and (node.number > right.number):
          sort(node, right)
        elif not node.is_playground and (node.data > right.data):
          sort(node, right)
        else:  
          node = node.right 

class Node:
  def __init__(self, data, childs):
    self.data = data
    self.left = None
    self.right = None
    
    self.childs = childs
    self.number = int(data.split(" ")[1]) if "Praça" in data else 0
    self.is_playground = "Praça" in data

class Queue:
  def __init__(self):
    self.head = None
    self.last = None
    self.size = 0

  def insert(self, data, childs = None):
    node = Node(data, childs)
    
    if self.head is None:
      self.head = node 
      self.last = node 
    else:
      self.last.right = node
      node.left = self.last
      self.last = node

    self.size += 1

playgrounds = Queue()
size_playgrounds = int(input())

try:
  while True:
    playground = input().split(": ")
    childs = Queue()

    for child in playground[1].split(" "):
      childs.insert(child)

    bubble_sort(childs)
    
    playgrounds.insert(playground[0], childs)
except:
  bubble_sort(playgrounds)
  show_playgrounds(playgrounds)

