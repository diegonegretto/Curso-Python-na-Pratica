"""
2. Manipulação de Strings - DNA
Faça um programa em Python que recebe uma string que representa uma cadeia de DNA e
gera a cadeia complementar.
Exemplo:
Entrada: AATCTGCAC
Saída: TTAGACGTG
"""

cadeia_dna = input("Informe a cadeia de DNA:")
cadeia_dna = cadeia_dna.lower()

cadeia_dna = cadeia_dna.replace("a","T")
cadeia_dna = cadeia_dna.replace("t","A")
cadeia_dna = cadeia_dna.replace("g","C")
cadeia_dna = cadeia_dna.replace("c","G")

print("Cadeia Complementar: " + cadeia_dna.upper())
