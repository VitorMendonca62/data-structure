class TableHash:
  def __init__(self, teams):
    self.table = []
    self.limit = 10
    for _ in range(self.limit): self.table.append("vago")
    self.teams = teams
    self.insert()
    
  def calculate_hash(self, team):
    value_ascii = self.calculate_ascii(team)
    return value_ascii % 10
    
  def calculate_ascii(self, team):
    total = 0
    for member in team.data:
      total += ord(member)
    return total
    
  def insert(self):
    team = teams.head
    
    while team:
      value_hash = self.calculate_hash(team)
      
      if self.table[value_hash] != "vago":
        stop = False
        while (value_hash < self.limit) and (self.table[value_hash] != "vago") and not stop:
          value_hash = value_hash + 1 if value_hash  + 1 < 10 else 0
          if self.table[value_hash] == "vago":
            self.table[value_hash] = team.data
            stop = True
      else:
        self.table[value_hash] = team.data
      team = team.right
    print(self.table)

class Team:
  def __init__(self, data = []):
    self.data = data
    self.right = None

class Teams:
  def __init__(self, members):
    self.members = members
    self.head = None
    self.insert()
    
  def insert(self):
    members = self.members
    
    for member in members:
      team = self.head
      left = None
      is_in_team = False

      while team:
        left = team
        if member in team.data:
          is_in_team = True
        team = team.right      

      if is_in_team:
        if member not in left.data:
          left.data.append(member)
        else:
          left.right = Team([member])
      else:
        if self.head is None: 
          self.head = Team([member])
        else: 
          left.data.append(member)
  

members = list(input())

teams = Teams(members)
TableHash(teams)


