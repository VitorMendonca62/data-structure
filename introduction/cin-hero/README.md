# Cin-Hero

##Problem Statement

A ONG CIn-Hero é uma instituição que salva animais perdidos pela cidade do Recife e divulga os bichinhos encontrados na internet. Sérgio, o presidente da organização, notou que havia diversos erros no código fonte do sistema de cadastramento dos pets. Para solucionar os empecilhos no sistema, foi confiado a você programador as seguintes tarefas:

- Consertar o código fonte já existente.
- Criar um método com 2 parâmetros raça e a data para remover o registro do animal. (comando 4 da legenda)


###Contexto:
Você receberá inputs de 1 a 5 onde cada número corresponde/realiza um comando dentro do sistema do CIn-Hero.

Legenda de Comandos:

1 - Cadastrar

2 - Imprimir relatório

3 - Imprimir os animais depois de uma data

4 - Remover um animal

5 - Finaliza o código

Obs: o conserto e todos os códigos adicionais devem seguir a lógica de POO(programação orientada a objetos). Note que o código também viola os princípios SOLID (qual?/quais?), mas você não precisa se preocupar com isso, apenas faça o conserto mínimo necessário para obter o funcionamento solicitado.
Código defeituoso:

```python
class Animal:

def __init__(self):
    self.listaAnimais = []

def cadastro(local, raca, data):
    listaAnimais.append((local, raca, data))

def imprimeRelatorio():
    for animal in listaAnimais:
        print(f"Local: {animal[0]}\nRaça: {animal[1]}\nData: {animal[2]}\n")

def dataInteresse(data):
    diaI, mesI, anoI = data.split("/")

    for animal in listaAnimais:
        dia, mes, ano = animal[2].split("/")

        if int(ano) > int(anoI):
            print("Local encontrado:", animal[0], "- Raça:", animal[1], "- Data:", animal[2])
            print()

        elif int(ano) == int(anoI) and int(mes) > int(mesI):
            print("Local encontrado:", animal[0], "- Raça:", animal[1], "- Data:", animal[2])
            print()
            
        elif int(ano) == int(anoI) and int(mes) == int(mesI) and int(dia) > int(diaI):
            print("Local encontrado:", animal[0], "- Raça:", animal[1], "- Data:", animal[2])
            print()

 def removerAnimal(raca, data):
      #refazer esta parte
      pass
while True:

entrada = input()

if entrada == "1":
    registros = input().split()
    sistema.cadastro(registros[0], registros[1], registros[2])
    
elif entrada == "2":
    sistema.imprimeRelatorio()
    
elif entrada == "3":
    data = input()
    sistema.dataInteresse(data)
    
elif entrada == "4":
    remover = input().split()
    sistema.removerAnimal(remover[0], remover[1])
    
elif entrada == "5":
```
##Input

> Se o comando for 1 a entrada deve ser dada da seguinte forma : local(espaço)raça(espaço) data

> Se o comando for 2 o output deverá ser a lista completa de todos os animais resgatados nos respectivos locais e nas respectivas datas.

> Se o comando for 3, você receberá como entrada uma data logo abaixo e em seguida o output deverá retornar todos os animais registrados após esta data.

> Se o comando for 4 você receberá abaixo a raça do animal e a data que foi encontrado e o removerá.

###Exemplo:

4

poodle 20/05/2022

Se o comando for 5 o sistema será finalizado.

##Output

> Se o comando for 2 você deverá imprimir a lista de todos os resgatados

Exemplo:

Local: LOCAL

Raça: RAÇA

Data: xx/yy/xxyy

> Se o comando for 3 você deverá imprimir os animais após a data.

Exemplo:

Local encontrado: LOCAL - Raça: RAÇA - Data: xx/yy/xxyy

##Examples

Case: 1

```
Input
2
1
UFPE Pitbull 10/08/2022
2
1
UPE Labrador 10/07/2022
2
3
10/07/2022
4
Labrador 10/07/2022
2
5

Output
Local: UFPE
Raça: Pitbull
Data: 10/08/2022

Local: UFPE
Raça: Pitbull
Data: 10/08/2022

Local: UPE
Raça: Labrador
Data: 10/07/2022

Local encontrado: UFPE - Raça: Pitbull - Data: 10/08/2022

Local: UFPE
Raça: Pitbull
Data: 10/08/2022
```