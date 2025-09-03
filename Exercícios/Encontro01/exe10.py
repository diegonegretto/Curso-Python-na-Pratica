"""
10. Média com quantidade indefinida
Peça ao usuário para digitar vários números até que ele digite `0`. Depois, mostre a média dos números digitados.
"""

numero = int(input("Informe um numero: "))
contador = 0
soma = 0

while numero != 0:
    contador += 1
    soma += numero
    numero = int(input("Informe um numero: "))

media = soma / contador

print(f"A media dos numeros digitados é: {media}")