# Manipulação de Arquivos em Python
# ----------------------------------

# Escrita (sobrescreve se já existir)
with open("dados.txt", "w") as arquivo:
    arquivo.write("Primeira linha\n")
    arquivo.write("Segunda linha\n")

# Leitura de todo o conteúdo
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:")
    print(conteudo)

# Leitura linha a linha
with open("dados.txt", "r") as arquivo:
    for linha in arquivo:
        print("Linha:", linha.strip())

# Acrescentar conteúdo sem apagar o existente
with open("dados.txt", "a") as arquivo:
    arquivo.write("Nova linha adicionada\n")

    