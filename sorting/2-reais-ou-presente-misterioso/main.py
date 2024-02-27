
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
  
  def to_double(self):
    node = self.head
    
    while node:
      node.data *= 2
      node = node.right
  
  def show(self):
    result = []
    node = self.head
    
    while node:
      result.append(node.data)
      node = node.right
    
    print(result)
  
  def insertion_sort(self):
    size = self.size
    
    node = self.head
    node = node.right
    
    for i in range(1,size):  
      next_node = node.right
      j = i - 1
      
      left = node.left
      real_left = None
      last_left = left
      
      while j >= 0 and left.data > node.data:
        real_left = left
        left = left.left
        j -= 1
      
      left = real_left if real_left != None else left
      
      if left.data > node.data:
        if left is self.head:
          self.head = node
        if node is self.last:
          self.last = node.left
          self.last.right = None
          
        if left.left:
          left.left.right = node
        if node.right:
          last_left.right = node.right
          node.right.left = last_left
          
        node.left = left.left
        left.left = node
        node.right = left

      node = next_node

  def quick_sort(self, left, right):
    
    def partition(low, high):
      node = self.head
      index_node = 0
      
      for _ in range(low):
        index_node += 1  
        node = node.right

      aux = node
      index_aux = index_node
      for _ in range(high - low):
        index_aux += 1
        aux = aux.right

      for _ in range(high):        
        condition_back = index_node < index_aux 
        condition_post = index_node > index_aux 
        
        condition_back_and_bigger = condition_back and (node.data > aux.data)
        condition_back_and_smaller = condition_post and (node.data < aux.data)
        
        if condition_back_and_bigger or condition_back_and_smaller:
          node.data, aux.data = aux.data, node.data
        if node.data != aux.data:
          condition_back = index_node < index_aux 
          condition_post = index_node > index_aux 
          
          if condition_back:
            aux = aux.left
            index_aux -= 1
          elif condition_post:
            aux = aux.right
            index_aux += 1
      return index_node

    if left < right:

      index = partition(left, right)
      
      if index is not None:
        self.quick_sort(left, index - 1)
        self.quick_sort(index + 1, right)

  def merge_sort(self, size, init_first_half = None, final_half = None, size_first_half = 1, size_last_half = 0 ):
    
    if size > 1:
      if init_first_half is None: init_first_half = self.head
      if final_half is None: final_half = self.last
      
      mid = size // 2
      
      last_left_half = init_first_half
      
      for _ in range(mid - 1):
        last_left_half = last_left_half.right
        size_first_half += 1
        
      init_last_half = last_left_half.right  
      last_right_half = last_left_half
      
      for _ in range(size - mid):
        last_right_half = last_right_half.right
        size_last_half += 1
      
      
      lasts = self.merge_sort(size_first_half, init_first_half, last_left_half)
      if lasts:
        init_first_half, last_left_half = lasts
        
      lasts = self.merge_sort(size_last_half, init_last_half, last_right_half)
      if lasts:
        init_last_half, last_right_half = lasts
        
      i = 0
      j = 0
      
      left = init_first_half
      right = init_last_half
      
      while i < size_first_half and j < size_last_half:
        if left.data < right.data:
          i += 1
          if left.right != right:
            left = left.right
          else:
            left = right.right
        elif left.data > right.data:
          next_right = right.right 
          right_left = right.left
          
          if left == self.head:
            self.head = right
          if right == self.last:
            self.last = left
            self.last.right = None
          
          if left.left:
            left.left.right = right
            
          right.left = left.left
          left.left = right
          
          if size == 2:
            left.right = right.right
            if right.right:
              right.right.left = left
          else:
            if right.right:
              right.right.left = right_left
              right_left.right = right.right
            
          if size_first_half == 1 or left.right == right :
            left.right = right.right
            
          right.right = left
          if left == init_first_half:
            init_first_half = right
          if right == last_right_half:
            last_right_half = left
          
          right = next_right
          j += 1
          
      return init_first_half, last_right_half
  
  def shell_sort(self):
    size = self.size
    gap = size // 2
    
    while gap > 0:
      for i in range(gap, size):
        node = self.head
        temp = self.head
        
        for _ in range(i):
          node = node.right
          
        j = i

        for _ in range(j - gap):
          temp = temp.right

        value_node = node.data
        
        while j >= gap and value_node <= temp.data:
          node.data, temp.data = temp.data, node.data
          node = temp
          
          j -= gap
          
          temp_2 = self.head
          for _ in range(j):
            temp_2 = temp_2.right
          
          if temp_2.data >= value_node:
            node.data, temp_2.data = temp_2.data, node.data
            temp = temp_2
            node = temp
        
      gap //=2

  def selection_sort(self):
    size = self.size
    
    node = self.head
    for _ in range(size):
      temp = node.right
      while temp:
        if node.data > temp.data:
          node.data, temp.data = temp.data, node.data
        temp = temp.right
      node = node.right
    
input_numbers = input().split(", ")
numbers = Queue()

for number in input_numbers:
  numbers.insert(int(number))

type_sort = input().lower().replace(" ", "_")
  
sorts = {
  "quick_sort": numbers.quick_sort,
  "merge_sort": numbers.merge_sort,
  "shell_sort": numbers.shell_sort,
  "selection_sort": numbers.selection_sort,
  "insertion_sort": numbers.insertion_sort,
}

sort = sorts[type_sort]

if type_sort == "quick_sort": sort(0, numbers.size-1)
elif type_sort == "merge_sort" : sort(numbers.size)
else: sort()

is_double = input() == "dobre!"

if is_double:
  numbers.to_double()

numbers.show()