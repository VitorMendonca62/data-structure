
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class Queue:
  def __init__(self):
    self.head = None
    self.last = None
    self.size = 0
    self.sla = []

  def insert(self, data):
    node = Node(data)
    
    if self.head is None:
      self.head = node 
      self.last = node 
    else:
      self.last.right = node
      node.left = self.last
      self.last = node

    self.size += 1
  
  def show(self):
    result = []
    node = self.head
    
    while node:
      result.append(node.data)
      node = node.right
    
    print(result)
    
  def heapify(self, size, index):
      left = 2 * index + 1
      right = 2 * index + 2
      largest = index
      
      elem_index = self.head
      
      if index != 0:
        for _ in range(index):
          elem_index = elem_index.right
      
      elem_largest = elem_index
      
      if left < size:
        child_left = elem_index
        vezes = left - index
        for _ in range(vezes):
          child_left = child_left.right
        
        if child_left.data < elem_index.data:
          elem_largest = child_left
          largest = left

      if right < size:
        child_right = child_left.right
        
        if child_right.data < elem_largest.data:
          elem_largest = child_right
          largest = right   

      if largest != index:
        elem_index.data, elem_largest.data = elem_largest.data, elem_index.data
        self.heapify(size, largest)

  def heapsort(self):
    size = self.size
    
    if size > 2:
      for index in range(size // 2 - 1, -1, -1):
        self.heapify(size, index)
        
      for index in range(size - 1, 0, -1):
        elem_index = self.head
      
        if index != 0:
          for _ in range(index):
            elem_index = elem_index.right
              
        elem_index.data, self.head.data = self.head.data, elem_index.data
        self.heapify(index, 0)
    elif size != 0:
      if self.last.data > self.head.data:
        self.last.data, self.head.data = self.head.data, self.last.data, 
          

input_numbers = input().split(" ")
numbers = Queue()

for number in input_numbers:
  numbers.insert(int(number))

first = input_numbers[0]

numbers.heapsort()

largest = numbers.head.data

print(f"Atenção, Grinch está indo atrás do cidadão de {largest} anos, e logo após isso ele vai atrás do cidadão de {first} anos.")