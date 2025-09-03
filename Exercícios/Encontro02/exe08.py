"""
8. Funções – Números pares
Escreva uma função que receba uma lista de números e retorne apenas os números pares
"""

def numeros_pares(numeros):
    lista_pares = []
    for numero in numeros:
        if numero%2 == 0:
            lista_pares.append(numero)
    
    return lista_pares


lista_numeros = [1,2,3,4,5]
pares = numeros_pares(lista_numeros)
print(pares)