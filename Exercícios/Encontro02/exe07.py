"""
7. Funções – Cálculo de área
Escreva uma função que receba a base e a altura de um triângulo e retorne sua área.
"""

def calcular_area(base, altura):
    return (base*altura)/2

base = float(input("Informe o valor da base do triângulo:"))
altura = float(input("Informe o valor da altura do triângulo:"))

area_triangulo = calcular_area(base, altura)

print("Área do Triângulo:", area_triangulo)