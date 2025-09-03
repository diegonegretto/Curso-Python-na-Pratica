"""
6. Tabuada
Peça ao usuário um número e mostre a tabuada desse número de `1` a `10`.
"""

numero = int(input("Informe o numero: "))

for i in range(11):
    print(f"{numero} x {i} = {numero*i}")