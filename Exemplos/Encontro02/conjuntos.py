# Conjuntos em Python
# -----------------

# Criando conjuntos
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = set() # Conjunto vazio

# Adicionar e remover elementos
A.add(7)          # Adiciona um elemento
A.remove(2)       # Remove o elemento 2 (erro se não existir)
A.discard(10)     # Remove sem erro, mesmo que não exista
print("A:", A)

# União
print("União:", A.union(B))       # {1, 3, 4, 5, 6, 7}
print("União (|):", A | B)        # forma reduzida

# Interseção
print("Interseção:", A.intersection(B))  # {3, 4}
print("Interseção (&):", A & B)

# Diferença
print("Diferença:", A.difference(B))     # Elementos de A que não estão em B
print("Diferença (-):", A - B)

# Diferença simétrica
print("Dif. Simétrica:", A.symmetric_difference(B))  # {1, 5, 6, 7}
print("Dif. Simétrica (^):", A ^ B)

# Verificação de subconjunto e superconjunto
print("A é subconjunto de B?", A.issubset(B))
print("A é superconjunto de B?", A.issuperset(B))

# Testar se não há elementos em comum
print("A e B são disjuntos?", A.isdisjoint(B))

