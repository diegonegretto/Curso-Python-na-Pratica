"""
9. Manipulação de arquivos – Registro de Nomes
Crie um programa que:
• Peça nomes ao usuário e salve-os em um arquivo nomes.txt;
• Depois, abra o arquivo e mostre todos os nomes na tela.

"""

with open("nomes.txt", "w") as arquivo:
    while True:
        nome = input("Digite um nome (ou ENTER para sair): ")
        if nome == "":
            break
        arquivo.write(nome+"\n")

print("Lista de nomes cadastrados:")
with open("nomes.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip()) #remove espaços em branco extras no começo e no fim da string, incluindo a quebra de linha \n.