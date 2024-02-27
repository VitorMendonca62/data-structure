class Vertice:
  def __init__(self, data, number, weight):
    self.weight = weight
    self.data = data
    self.number = number
    self.pointers = []

class Graph:
  def __init__(self, vertices):
    self.vertices = vertices
    self.nodes = [False for _ in range(vertices)]
  
  def is_in_graph(self, port):
    if port <= self.vertices:
      return self.nodes[port - 1]
    return False
  
  def add_vertice(self, user, connection):
    if not self.is_in_graph(user):
      initial_node = Vertice(f"v{user}", user, 1)
      self.nodes[user - 1] = initial_node
    else: 
      initial_node =  self.nodes[user - 1]

    if not self.is_in_graph(connection):
      node = Vertice(f"v{connection}", connection, 1)
    else:
      node = self.nodes[connection - 1]
      
    initial_node.pointers.append(node)
    node.pointers.append(initial_node)
      
    self.nodes[user - 1] = initial_node
    self.nodes[node.number - 1] = node

  def search_know_news(self, node):
    searched = [node]
    
    def recursion(pointers, know):
      for pointer in pointers:
        if pointer not in searched:
          searched.append(pointer)
          know = recursion(pointer.pointers, know + 1)
          
      return know 
    
    return recursion(node.pointers, 1)      

users_size, connections = input().split(" ")
users_size, connections = int(users_size), int(connections)

graph = Graph(users_size)

for _ in range(connections):
  user, connection = input().split(" ")
  user, connection = int(user), int(connection)
  graph.add_vertice(user,connection)

result = []
for node in graph.nodes:
  result.append(graph.search_know_news(node) if node else 1)

print(*result)