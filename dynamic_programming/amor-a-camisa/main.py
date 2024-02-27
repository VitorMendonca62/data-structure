# Tava pesquisando mais a fundo e encontrei um artigo falando sobre tecnicas de programacao dinamica
# Se eu não me engano se chama memorização.

def sum_total(i, cache, sectores):
  if i < 0:
    return 0
  
  if cache[i] > -1:
    return cache[i]
  
  cache[i] = max(sectores[i] + sum_total(i - 2, cache, sectores), sum_total(i - 1, cache, sectores))
  print(cache)
  return cache[i]
    
size = int(input())

str_sectores = input().split(" ")

sectores = []

for sector in str_sectores:
  sectores.append(int(sector))

sum_total_returned = sum_total(size - 1, [-1] * size, sectores)
print(sum_total_returned, "torcedores podem ser fotografados.")