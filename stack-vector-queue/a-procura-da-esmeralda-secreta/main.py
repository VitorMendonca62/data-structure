class Numero:
  def __init__(self, data):
    self.data = data
    self.next = None

class ListaLinkada:
  def __init__(self):
    self.cabecao = None
    self.size = 0
  
  def adicionar(self, elem):
    # Se ele ja tiver uma cabeça, ele pecorre ate a ultimo ponteiro e 
    # e aponta esse uultimo para um novo ponteiro
    # Caso nao tenha, ele coloca um novo ponteiro como a cabeca
    if self.cabecao:
      ponteiro = self.cabecao
      while ponteiro.next:
        ponteiro = ponteiro.next
      ponteiro.next = Numero(elem)
    else:
      self.cabecao = Numero(elem)
    self.size += 1
    print(f"Node {elem} adicionado")
    
  def remover(self, elem):
    ponteiro = self.cabecao
    anterior = None
    
    while (ponteiro) and (ponteiro.next and ponteiro.data != elem):
      anterior = ponteiro
      ponteiro = ponteiro.next
      
    if (ponteiro) and (ponteiro.next or not ponteiro.data != elem):
      if anterior:
        anterior.next = ponteiro.next if ponteiro.next else None 
      else:
        self.cabecao = ponteiro.next 
      self.size -= 1
      print(f"Node {elem} foi removido")
    else: 
      print(f"Node {elem} não existe")


  def empurrar(self, elem):
    ponteiro = self.cabecao
    anterior = None
    
    while (ponteiro) and (ponteiro.next and ponteiro.data != elem):
      anterior = ponteiro
      ponteiro = ponteiro.next

    if (ponteiro) and (ponteiro.next or not ponteiro.data != elem):
      elemento = ponteiro
      proximo = ponteiro.next
      if proximo:
        elemento.next = proximo.next
        proximo.next = elemento
        print(f"Node {elem} empurrado")
        if anterior: 
          anterior.next = proximo
        else:
          self.cabecao = proximo
      else: 
        print(f"Não existe Node depois de {elem}")
    else: 
      print(f"Node {elem} não existe")
  
  def puxar(self, elem):
    ponteiro = self.cabecao
    anterior = None
    anterior_anterior = None
    
    while (ponteiro) and (ponteiro.next and ponteiro.data != elem):
      anterior_anterior = anterior
      anterior = ponteiro
      ponteiro = ponteiro.next
    
    if (ponteiro) and (ponteiro.next or not ponteiro.data != elem):
      elemento = ponteiro
      if anterior: 
        anterior.next = elemento.next
        elemento.next = anterior
        print(f"Node {elem} puxado")
      else:
        print(f"Não existe Node antes de {elem}")
      # Caso nao tenha anterior do anteriro, ent ele vai ser a cabeça 
      if anterior_anterior:
        anterior_anterior.next = elemento
      else: 
        self.cabecao = elemento
  
    else: 
      print(f"Node {elem} não existe")

  def finalizar(self):
    ponteiro = self.cabecao
    string = "mapa:"
    
    # se o ponteiro tiver next, ele pega o valor e adiciona na string, depois
    # pega o next do ponteiro
    if ponteiro:
      while ponteiro.next:
        string += f"{ponteiro.data}->"
        ponteiro = ponteiro.next
      string += f"{ponteiro.data}"
    print(string)
      
lista = ListaLinkada()
parar = False

while not parar:
  instrucao = input()
  if instrucao != "fim!":
    numero, instrucao = instrucao.split(":")
  
  if instrucao == "adicione-me!":
    lista.adicionar(numero)
  if instrucao == "remova-me!":
    lista.remover(numero)
  if instrucao == "empurre-me!":
    lista.empurrar(numero)
  if instrucao == "puxe-me!":
    lista.puxar(numero)
  if instrucao == "fim!":
    lista.finalizar()
    parar = True