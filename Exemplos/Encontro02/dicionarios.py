# Dicionários em Python
# -----------------

# Criando um dicionário com alguns elementos (nome, idade e profissão)
meu_dicionario = {"nome": "Diego", "idade": 35, "profissao":"Professor"}
print(meu_dicionario)

# Buscando um elemento a partir de uma chave.
print(meu_dicionario["nome"])
# Buscando um elemento a partir de uma chave com o metodo get.
print(meu_dicionario.get("profissao"))
# Removendo um elemento do dicionario a partir de uma chave.
print(meu_dicionario.pop("idade"))
print(meu_dicionario)

# Imprimindo somente as chaves do dicionario
print(meu_dicionario.keys())
# Imprimindo somente os valores do dicionario
print(meu_dicionario.values())
# Apagando todo o conteúdo do dicionario
meu_dicionario.clear()
print(meu_dicionario)

# Exemplo de dicionairos mais complexos
# Criação de um dicionario com outros dicionarios dentro
pessoa = {
    "nome": "Diego",
    "idade": 35,
    "profissao": "Professor",
    "interesses": ["Python", "Literatura", "Games"],
    "pet":{
        "nome": "Mei",
        "idade": 8,
        "peso": "7kg"
    }
}

print(pessoa)
print(pessoa.get("nome"))
print(pessoa["nome"])
print(pessoa.get("interesses"))
print(pessoa.get("interesses")[0])
print(pessoa["interesses"][0])
print(pessoa.get("pet").get("nome"))
print(pessoa["pet"]["nome"])

# Adicionando dado no dicionario
pessoa["ano_nascimento"] = 1989
print(pessoa)
# Adicionando uma lista no dicionario com chave cores_favoritas
pessoa["cores_favoritas"] = ["Azul", "Preto", "Verde"]
print(pessoa)
# Adicionando um dicionario dentro do dicionario com chave mãe.
pessoa["mae"] = {
    "nome":"Maria",
    "idade": 60
}
print(pessoa)

