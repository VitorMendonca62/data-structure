class Node:
    def __init__(self, data):
        camisas = ["endrick", "neymar", "cr7", "messi",]
        chuteiras = ["new balance", "puma", "nike", "adidas",]
        camisas_e_chuteiras = {"camisas": camisas, "chuteiras": chuteiras}

        self.data = data
        self.next = None

        categoria = "camisas" if data in camisas else "chuteiras"
        index = camisas_e_chuteiras[categoria].index(data)
        
        categoria_equivalente = "camisas" if categoria == "chuteiras" else "chuteiras"
        self.categoria = categoria
        self.equivalente = camisas_e_chuteiras[categoria_equivalente][index]


class Pilha:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def pop(self):
        if self.is_empty():
            return None
        popped = self.head.data
        self.head = self.head.next
        return popped

    def verificar_pilha(self, correto):
        pointer = self.head

        if (pointer and pointer.next):
            equivalente = pointer.equivalente
            anterior = None

            while pointer.next and pointer.data != equivalente:
                anterior = pointer 
                pointer = pointer.next
            
            if (correto) and (pointer) and (pointer.next or not pointer.data != equivalente) and self.head.categoria == "chuteiras":
                self.pop()
                if anterior and anterior.data != pointer.equivalente:
                    anterior.next = pointer.next
                else:
                    self.head = pointer.next
                correto = self.verificar_pilha(correto)
            else:
                correto = False
            return correto
        elif self.head == None:
            return correto
        else: correto = False

strings = input().split("-")
pilha = Pilha()

for string in strings:
    pilha.push(string)

print("Correto" if pilha.verificar_pilha(True) else "Incorreto")