class TableHash:
  def __init__(self):
    self.table = []
    self.limit = 10
    for i in range(self.limit):
      self.table.append(Team(i+1))
    self.result = []

  def insert(self, name, number):
    self.table[number-1].insert(name)
        
  def alphabetical_order(self): 
    def heapify(team, size, index):
      left = 2 * index + 1
      right = 2 * index + 2
      largest = index
      
      elem_index = team.head
      
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
        heapify(team, size, largest)

    def heapsort(team):
      size = team.size
      
      if size > 2:
        for index in range(size // 2 - 1, -1, -1):
          heapify(team, size, index)
          
        for index in range(size - 1, 0, -1):
          elem_index = team.head
        
          if index != 0:
            for _ in range(index):
              elem_index = elem_index.right
                
          elem_index.data, team.head.data = team.head.data, elem_index.data
          heapify(team, index, 0)
      elif size != 0:
        if team.last.data > team.head.data:
          team.last.data, team.head.data = team.head.data, team.last.data, 
          
    for team in self.table:
      heapsort(team)
  
  def show(self):
    for column in self.table:
      if column.head is not None:
        number =  column.number
        node = column.last
        for index in range(1, column.size+1):
          if number > 1:
            if index % number == 1:
              self.result.append([node.data])
            else:
                self.result[-1].append(node.data)
          else:
            self.result.append([node.data])
            
          node = node.left
    print(self.result)
        
    
class Member:
  def __init__(self, data = []):
    self.data = data
    self.right = None
    self.left = None

class Team:
  def __init__(self, number):
    self.head = None
    self.last = None
    self.size = 0
    self.number = number

  def insert(self, name):
    node = self.head
    left = None
    
    member = Member(name)
    
    if self.head is None:
      self.head = member
    else:
      while node:
        left = node
        node = node.right
    
      left.right = member
      member.left = left
      
    self.last = member
    self.size += 1
  
table = TableHash()
try:
  while True:
    name, number = input().split(" ")
    number = int(number)
    table.insert(name, number)
except:
  table.alphabetical_order()
  table.show()




