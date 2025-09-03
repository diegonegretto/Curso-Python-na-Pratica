"""
1. Operações básicas
Crie uma calculadora simples a partir de dois números e da operação informada pelo
usuário. Operações disponíveis:
- 1- soma
- 2- subtração
- 3- multiplicação
- 4- divisão real
- 5- divisão inteira
- 6- resto da divisão
- 7- potência
"""


print("Calculadora Simples")
print("Escolha a operação:")
print("1- Soma")
print("2- Subtração")
print("3- Multiplicação")   
print("4- Divisão real")
print("5- Divisão inteira")
print("6- Resto da divisão")
print("7- Potência")    
operacao = input("Digite o número da operação: ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if operacao == '1':
    resultado = num1 + num2
    print(f"O resultado da soma é: {resultado}")

elif operacao == '2':
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado}")
    
elif operacao == '3':
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")

elif operacao == '4':
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado da divisão real é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
    
elif operacao == '5':
    if num2 != 0:
        resultado = num1 // num2
        print(f"O resultado da divisão inteira é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
    
elif operacao == '6':       
    if num2 != 0:
        resultado = num1 % num2
        print(f"O resultado do resto da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")

elif operacao == '7':
    resultado = num1 ** num2
    print(f"O resultado da potência é: {resultado}")
    
else:
    print("Operação inválida. Por favor, escolha uma operação entre 1 e 7.")
# Fim do programa