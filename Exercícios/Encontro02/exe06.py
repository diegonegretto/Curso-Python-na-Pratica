"""
6. Conjuntos – Números únicos
Peça para o usuário digitar 10 números (pode repetir).
• Armazene-os em um conjunto;
• Mostre quais números foram digitados sem repetição.
"""

numeros_unicos = set()

for i in range(11):
    numero = int(input("Informe um número:"))
    numeros_unicos.add(numero)

print(numeros_unicos)