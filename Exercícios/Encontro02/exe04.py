"""
4. Tuplas – Meses do ano
Crie uma tupla com os 12 meses do ano.
• Peça para o usuário digitar um número de 1 a 12 e mostre qual mês corresponde.
"""

meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

numero = int(input("Informe um número de mês:"))
print(meses[numero-1])