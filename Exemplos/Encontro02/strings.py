# Strings em Python
# -----------------

texto = "Curso Python Na Prática"

# Mostra o caractere na posição 0
print(texto[0])
# Mostra os caracteres do índice 5 até 11
print(texto[5:12])
# Mostra do índice 5 até o fim
print(texto[5:])
# Mostra do início até o índice 4
print(texto[:5])

# Mostra o tamanho da string (número de caracteres, incluindo espaços).
print(len(texto))

# Conta quantas vezes aparece o caractere "A" (maiúsculo).
print(texto.count("A"))
# Conta quantas vezes aparece o caractere "a" (minúsculo).
print(texto.count("a"))
# Conta quantos "P" existem entre os índices 5 e 11.
print(texto.count("P", 5, 12))

# Mostra a posição inicial da palavra "Curso"
print(texto.find("Curso"))
# Mostra a posição inicial da palavra "Python"
print(texto.find("Python"))

# Converte toda a string para maiúsculas.
print(texto.upper())
# Converte toda a string para minúsculas.
print(texto.lower())

# Deixa só a primeira letra da string em maiúscula.
print(texto.capitalize())
# Deixa a primeira letra de cada palavra em maiúscula.
print(texto.title())

# Divide a string em uma lista de palavras, usando os espaços como separador.
print(texto.split())
# Armazena essa lista de palavras na variável lista_de_palavras.
lista_de_palavras = texto.split()
# Junta as palavras da lista sem espaços
print(''.join(lista_de_palavras))

texto = "    CURSO PYTHON       "
print(texto)
# Remove os espaços do início e do fim.
print(texto.strip())
# Remove apenas os espaços da direita (fim da string).
print(texto.rstrip())
# Remove apenas os espaços da esquerda (início da string).
print(texto.lstrip())

texto = "Eu gosto de Java"
print (texto)
# Substitui "Java" por "Python"
novo_texto = texto.replace("Java", "Python")
print(novo_texto)

