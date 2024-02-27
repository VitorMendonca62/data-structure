global_words = input().split(", ")
global_words.sort()

res = set()

def backtracking(permutation, words):
  if not words:
    res.add(permutation)
    return

  new_permutation = []
  i = 0
  
  for word in words:
    i += 1
    res.add(permutation)
    if len(permutation) == 0 or global_words.index(word) > global_words.index(permutation[0]):
      new_permutation = permutation + tuple([word])
      backtracking(tuple(new_permutation), words[i:])
        
if global_words[0] != " ":    
  backtracking((), global_words)
else:
  res.add(())

res = list(res)
res.sort()

for i in range(len(res)):
  res[i] = list(res[i])

print("O número de subsets de visitação é", len(res))
print("São eles:", res)

# Planeta Alpha, Planeta Beta, Planeta Gamma, Planeta Delta, Planeta Epsilon, Planeta Zeta 
# Planeta Alpha, Planeta Caito, Planeta Deito, Planeta Beta, Planeta Gamma, Planeta Delta, Planeta Epsilon, Planeta Zeta, Planeta Vitor, Planeta Laisa, Planeta Geydson