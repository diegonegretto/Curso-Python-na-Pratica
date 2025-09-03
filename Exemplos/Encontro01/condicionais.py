# Condicionais
# -----------------
condicao_verdadeira_ou_falsa = True
if condicao_verdadeira_ou_falsa:
    print("Entrou no if\n")
    #instrução_2
    #instrução_3
else:
    print("Não entrou no if\n")
    #instrução_5

print("Instrução fora da condicional!\n")

# Comandos if-else aninhados
# -----------------
x = 2
y = 5

if x > y:
    if x % 2 == 0:
        print("x é maior que y e é par!")
    else:
        print("x é maior que y e é ímpar!")
else:
    if y % 2 == 0:
        print("y é maior que x e é par!")
    else:
        print("y é maior que x e é ímpar!")


# Comando elif
# -----------------
media_final = 3.8

if media_final >= 5:
    print("Aprovado!")
elif media_final >= 3:
    print("RE!")
else:
    print("Reprovado!")