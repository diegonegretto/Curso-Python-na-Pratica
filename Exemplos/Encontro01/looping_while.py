# Looping While
# -----------------

numero = int(input("Informe um número inteiro ou -1 para parar: "))

while numero != -1:
    if numero%2 == 0:
        print("Número informado é par!\n")
    else:
        print("Número informado é ímpar!\n")
    
    numero = int(input("Informe um número inteiro ou -1 para parar: "))

print("Até logo!")

