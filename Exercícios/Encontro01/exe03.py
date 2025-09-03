"""
3. Classificação por idade
Peça a idade de uma pessoa e diga se ela é:
- Criança (0–12)
- Adolescente (13–17)
- Adulto (18–59)
- Idoso (60+)
"""

idade = int(input("Informe a idade: "))

if idade > 60:
    print("Idoso")
elif idade > 18:
    print("Adulto")
elif idade > 13:
    print("Adolescente")
elif idade >= 0:
    print("Criança")
else:
    print("Idade inválida!")