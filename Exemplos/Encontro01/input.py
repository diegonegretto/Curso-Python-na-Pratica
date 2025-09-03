# A função input()
# -----------------

# input() com um argumento
nome = input("Qual seu nome?\n")
print("Olá,",nome)

# Conversão de tipo float
numero = input("Digite um número: ")
# print(numero ** 2) # Essa linha vai dar erro
print(type(numero))

numero = float(numero)
print(numero ** 2)
print(type(numero))

# Conversão de tipo int
numero_inteiro = int(input("Digite um número: "))
print(type(numero_inteiro))

# Conversão de tipo string
numero = 10
print(type(numero))
numero = str(numero)
print(type(numero))

