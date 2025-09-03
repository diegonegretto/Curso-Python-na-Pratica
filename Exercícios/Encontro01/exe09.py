"""
9. Jogo de adivinhação
Crie um programa que sorteie um número de `1` a `100` e peça para o usuário adivinhar. O programa deve dar dicas: - Se o número digitado é **maior** ou **menor** que o sorteado. - O jogo continua até o usuário acertar.
"""
import random

numero_sorteado = random.randint(1,100)

numero_escolhido = int(input("Informe um numero: "))

while numero_sorteado != numero_escolhido:
    if numero_escolhido > numero_sorteado:
        print(f"O numero sorteado é menor que {numero_escolhido}")
    else:
        print(f"O numero sorteado é maior que {numero_escolhido}")
    
    numero_escolhido = int(input("Informe um numero: "))

print("Parabéns! Você acertou!")