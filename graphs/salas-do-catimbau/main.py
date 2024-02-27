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
  
  def add_vertice(self, coord, searched):
    if not searched:
      number_vertice = coord[0]
      initial_node = Vertice(f"v{number_vertice}", number_vertice, 1)
      self.nodes[initial_node.number - 1] = initial_node

      for port in coord[1:]:
        if port == "Tesouro":
          initial_node.data += "- Tesouro"
          return None, True
          
        if port <= self.vertices:
          if not graph.is_in_graph(port):
            node, searched = self.add_vertice(all_coords[port -1], searched)
            if searched: return None, True
          else:
            node = graph.nodes[port-1]  
            
          initial_node.pointers.append(node)

      all_coords[initial_node.number - 1] = []
      self.nodes[initial_node.number - 1] = initial_node
    
      return initial_node, searched
    
    return None, True
  
index = 0
all_coords = []
running = True

try:
  while running:
    instruction = input()
    if instruction != "Tesouro":
      ports = instruction.split(" ")
    
      all_coords.append([index + 1])
      for port in ports:
        all_coords[-1].append(int(port))
    
    elif instruction == "Tesouro":
      running = False
      all_coords.append([int(index + 1), "Tesouro"])
    index += 1

except:
  pass
  
graph = Graph(len(all_coords))
searched = graph.add_vertice(all_coords[0], False)[1]

if not searched:
  print("SEM TESOURO :(")
else:
  print("TESOURO :)")

