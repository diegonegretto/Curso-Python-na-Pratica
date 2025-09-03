# Declaração de uma variável do tipo string
nome_completo = "Anakin Skywalker"

# Declaração de uma variável do tipo inteiro
idade = 22

# Escrevendo o conteúdo da variável nome_completo concatenando
# com uma string.
print("Nome Completo:", nome_completo)
print("Nome Completo:" + nome_completo)

# A função a seguir causa erro, pois não é possível concatenar
# string e inteiro usando o +
# print("Idade:" + idade)
# Uma alternativa seria usar a ,
print("Idade:", idade)

# Usando f-strings para concatenação
print(f"{nome_completo} tem {idade} anos.")

