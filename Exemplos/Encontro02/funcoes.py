# Funções em Python
# -----------------

# Definindo uma função chamada somar que recebe dois parâmentos
def somar(a, b):
    resultado = a + b
    return resultado # a função retorna um valor para quem a chamou.

# Fazendo a chamada da função somar passando valores.
meu_resultado = somar(2,2)
print(meu_resultado)

# Exemplos mais complexos
# Definindo uma função chamada envia_email que recebe dois parâmetros.
def envia_email(nome, email):
    nome_dest = nome
    email_dest = email
    return (f"Email enviado para {nome_dest} - {email_dest}")

# Criação de uma lista de pessoas em que cada elemento é um dicionario com chaves email e valor.
pessoas = [
    {
        "nome" : "João",
        "email" : "joao@email.com"
    },
    {
        "nome" : "Maria",
        "email" : "maria@email.com"
    },
    {
        "nome" : "José",
        "email" : "jose@email.com"
    }
]

# Percorrendo todos os itens da lista e chamando a função envia_email para todos.
for pessoa in pessoas:
    email_enviado = envia_email(pessoa["nome"], pessoa["email"])
    print(email_enviado)

# Imprimindo todos os indices e elementos da lista
for indice, pessoa in enumerate(pessoas):
    email_enviado = envia_email(pessoa["nome"], pessoa["email"])
    print(f"{indice} - {email_enviado}")

    