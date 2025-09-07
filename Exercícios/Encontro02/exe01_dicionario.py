"""
1. Manipulação de Strings – Data Nascimento
- Faça um programa em Python que leia uma data de nascimento no formato dd/mm/aaaa e
imprima a data com o mês escrito por extenso.
Exemplo:
Entrada: data = 13/09/1989
Resultado: Você nasceu em 13 de setembro de 1989
""" 
# Resolução com Dicionários
meses = {1:"Janeiro",
         2:"Fevereiro",
         3:"Março",
         4:"Abril",
         5:"Maio",
         6:"Junho",
         7:"Julho",
         8:"Agosto",
         9:"Setembro",
         10:"Outubro",
         11:"Novembro",
         12:"Dezembro"}

data_nascimento = input("Informe a data de nascimento no formato dd/mm/aaaa:")
data_nascimento = data_nascimento.split("/")

numero_mes = int(data_nascimento[1])
print(f"Você nasceu em {data_nascimento[0]} de {meses[numero_mes]} de {data_nascimento[2]}")