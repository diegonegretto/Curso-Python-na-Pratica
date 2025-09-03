"""
1. Manipulação de Strings – Data Nascimento
- Faça um programa em Python que leia uma data de nascimento no formato dd/mm/aaaa e
imprima a data com o mês escrito por extenso.
Exemplo:
Entrada: data = 13/09/1989
Resultado: Você nasceu em 13 de setembro de 1989
"""
meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa):")
data_nascimento = data_nascimento.split("/")
print(f"Você nasceu em {data_nascimento[0]} de {meses[int(data_nascimento[1])-1]} de {data_nascimento[2]}")