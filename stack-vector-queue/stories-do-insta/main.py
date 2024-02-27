class Node:
  def __init__(self, data ):
    self.data = data
    self.next = None
    self.back = None

class ListaLinkada:
  def __init__(self):
    self.head = None
  
  def adicionar(self, elem):
    node = Node(elem)
    if self.head:
      node.next = self.head
      self.head.back = node
      self.head = node
    else :
      self.head = node
      
  def remover(self, elem):
    ponteiro = self.verificar_lista(elem)
      
    if ponteiro and ponteiro.data == elem:
      anterior = ponteiro.back
      proximo = ponteiro.next
      if anterior:
        anterior.next = ponteiro.next
      else:
        self.head = ponteiro.next 
      if proximo:
        proximo.back = anterior
  def verificar_lista(self, elem):
    ponteiro = self.head
    
    while ponteiro and ponteiro.data != elem:
      ponteiro = ponteiro.next
    
    if ponteiro and ponteiro.data == elem:
      return ponteiro
    else:
      return False

  def finalizar(self):
    ponteiro = self.head
    
    while ponteiro:
      print(ponteiro.data)
      ponteiro = ponteiro.next
      
lista = ListaLinkada()

instrucao = ""
while instrucao != "Mark fechou o instagram":
  instrucao = input()
  
  if "Mark deixou de seguir" not in instrucao and instrucao != "Mark fechou o instagram":
    nome = instrucao.split(" ")[-1]
    esta_na_lista = lista.verificar_lista(nome) 
    
    if esta_na_lista :
      lista.remover(nome)
      lista.adicionar(nome) 
    elif "Mark seguiu" in instrucao:
      lista.adicionar(nome)
  
  elif "Mark deixou de seguir" in instrucao:
    nome = instrucao.split(" ")[-1]
    lista.remover(nome)

lista.finalizar()

