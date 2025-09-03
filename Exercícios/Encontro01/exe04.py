"""
4. Maior número entre três
Peça três números ao usuário e informe qual é o maior deles
"""

x = int(input("Informe o primeiro número: "))
y = int(input("Informe o segundo número: "))
z = int(input("Informe o terceiro: "))

if x > y and x > z:
    print(f"{x} é o maior!")
elif y > x and y > z:
    print(f"{y} é o maior!")
else:
    print(f"{z} é o maior!")
    