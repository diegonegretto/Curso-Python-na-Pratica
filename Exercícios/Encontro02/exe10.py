"""
10. Tratamento de múltiplas exceções
Crie um programa que:
• Peça dois números ao usuário;
• Tente converter os valores para int;
• Realize a divisão do primeiro pelo segundo;
• Trate as seguintes situações:
   -  Se o usuário digitar algo que não é número → mostrar "Entrada inválida. Digite apenas números.";
   - Se o usuário tentar dividir por zero → mostrar "Erro: divisão por zero não é permitida.";
   - Use o finally para exibir "Programa encerrado." em qualquer caso.
"""

try:
    primeiro_numero = int(input("Informe o primeiro número:"))
    segundo_numero = int(input("Informe o segundo número:"))

    divisao = primeiro_numero / segundo_numero
    print(f"{primeiro_numero}/{segundo_numero} = {divisao}")
except ValueError:
    print("Valor inválido!")
except ZeroDivisionError:
    print("Divisão por zero!")
finally:
    print("Programa encerrado!")