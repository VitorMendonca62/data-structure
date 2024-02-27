from math import log10

def instrucoes_computadas(instrucoes, complexidade):
  logn = False
  if "2n" in complexidade: complexidade = complexidade.replace("2n", "2.n") 
  if "logn" in complexidade:  
    complexidade = complexidade.replace("logn", "")
    logn = log10(instrucoes)
    
  complexidade = complexidade.replace("n", str(instrucoes))

  if "^" in complexidade: complexidade = complexidade.replace("^", "**")
  if "." in complexidade: complexidade = complexidade.replace(".", "*")
  complexidade = f"{complexidade}{logn if logn else ""}"
  return float(eval(complexidade))

qtd_instrucoes = int(input())

nome_comp_1, capacidade_1, nome_1lg_1, complexidade_1  = input().split(" - ")
nome_comp_2, capacidade_2, nome_1lg_2, complexidade_2  = input().split(" - ")

instrucoes_1 = instrucoes_computadas(qtd_instrucoes, complexidade_1)
instrucoes_2 = instrucoes_computadas(qtd_instrucoes, complexidade_2)

velocidade_1 = round(instrucoes_1 / int(capacidade_1) , 2)
velocidade_2 = round(instrucoes_2 / int(capacidade_2), 2)

print(f"Velocidade do {nome_comp_1}: {velocidade_1:.2f} segundos")
print(f"Velocidade do {nome_comp_2}: {velocidade_2:.2f} segundos")
mais_rapido = nome_comp_1 if velocidade_1 < velocidade_2 else nome_comp_2
print(f"O {mais_rapido} foi mais rápido!")