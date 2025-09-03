# Listas em Python
# -----------------

# Criação de uma lista vazia
carros = []
# Adicionando os elementos Ka, Fusca e Fiesta na lista
carros.append("Ka")
carros.append("Fusca")
carros.append("Fiesta")
print(carros)
# Adicionando o elemento 10 (inteiro) na lista
carros.append(10)
print(carros)

# Criação de uma lista com valores
nomes = ["João", "Maria", "José"]
print(nomes)
# Adicionando valores no final da lista.
nomes.append("Joaquim")
print(nomes)
# Imprimindo o primeiro elemento da lista.
print(nomes[0])

# Inserindo um elemento novo na lista em uma posição.
nomes.insert(1, "Joana")
print(nomes)

# Removendo o ultimo elemento da lista.
nomes.pop()
print(nomes)
# Removendo um elemento em uma posição específica da lista.
del nomes[1]
print(nomes)
# Removento um elemento da lista pelo valor.
nomes.remove("Maria")
print(nomes)

# Contando quantos elementos "João" existem na lista
print(nomes.count("João"))

# Invertendo a ordem dos elementos da lista
nomes.reverse()
print(nomes)

nomes.append("Ana")
print(nomes)
# Ordenando os elementos da lista
nomes.sort()
print(nomes)

# Tuplas em Python (imutáveis)
# -----------------
#Criando uma tupla
cores = ("vermelho", "azul", "verde")
print(cores[1])

