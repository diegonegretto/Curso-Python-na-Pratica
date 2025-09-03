"""
7. Soma dos pares de 1 a 100
Some todos os números **pares** de `1` a `100` usando um laço `for`.
"""

soma_pares = 0

for i in range(101):
    if i%2 == 0:
        soma_pares += i

print(soma_pares)