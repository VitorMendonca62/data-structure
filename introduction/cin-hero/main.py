class Sistema:
    def __init__(self):
        self.listaAnimais = []

    def cadastro(self, local, raca, data):
        self.listaAnimais.append({
            "local": local,
            "raca": raca,
            "data": data
            })
        print(self.listaAnimais)

    def imprimeRelatorio(self):
        for animal in self.listaAnimais:
            local, data, raca = animal["local"], animal["data"], animal["raca"]
            print(f"Local: {local}\nRaça: {raca}\nData: {data}\n")

    def dataInteresse(self, data_interesse):
        def printarLocalEncontrado(local, raca, data):
            print(f"Local encontrado: {local} - Raça: {raca} - Data: {data}\n")     
            
        diaInteresse, mesInteresse, anoInteresse = data_interesse.split("/")
        diaInteresse, mesInteresse, anoInteresse = int(diaInteresse), int(mesInteresse), int(anoInteresse)

        for animal in self.listaAnimais:
            local, data, raca = animal["local"], animal["data"], animal["raca"]
            dia, mes, ano = data.split("/")
            dia, mes, ano = int(dia), int(mes), int(ano)
        
            if ano > anoInteresse: printarLocalEncontrado(local, raca, data)
            elif ano == anoInteresse and mes > mesInteresse: printarLocalEncontrado(local, raca, data)                
            elif ano == anoInteresse and mes == mesInteresse and dia > diaInteresse: printarLocalEncontrado(local, raca, data)
                
    def removerAnimal(self, raca, data):
        for animal in self.listaAnimais:
            if (animal["raca"] == raca) and (animal["data"] == data):
                self.listaAnimais.remove(animal)

sistema = Sistema()
sistema_online = True

while sistema_online:
    entrada = input()
    
    if entrada == "1":
        local, raca, data = input().split(" ")
        sistema.cadastro(local, raca, data)
    elif entrada == "2":
        sistema.imprimeRelatorio() 
    elif entrada == "3":
        data = input()
        sistema.dataInteresse(data)   
    elif entrada == "4":
        remover = input().split()
        sistema.removerAnimal(remover[0], remover[1])  
    elif entrada == "5":
        sistema_online = False