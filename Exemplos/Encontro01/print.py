# Isso é um comentário
# ------------------------------------------
# Exemplos de utilização da função print()

print("Hello World!")

# \n é o símbolo especial para caractere de nova linha
print("Curso de Python!\nBem-vindos!")

# Escrevendo "Python" entre aspas
print("Curso de \"Python\"!")

# Usando vários argumentos (a função print() coloca um espaço entre 
# os argumentos gerados por sua própria iniciativa)
print("Curso","de","Python!")

# O argumento end=" " faz com que a função print() coloque um espaço
# em branco ao final da linha ao invés de um \n (implicito)
print("Curso de Python.", end=" ")
print("FHO Qualifica")

# O arqgumento sep="_" coloca um _ após cada palavra.
print("Curso","de","Python!",sep="_")

# Misturando os argumentos sep e end em uma mesma chamada.
print("Curso","de","Python", sep="_", end="!")
print("FHO", "Qualifica",sep="-",end="*\n")

# Repetindo a frase "Curso de Python!" cinco vezes
print("Curso de Python!\n" * 5)

# Python como calculadora
print(2+2)

