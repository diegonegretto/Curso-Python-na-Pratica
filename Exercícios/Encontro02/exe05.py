"""
5. Dicionários – Cadastro de aluno
Crie um dicionário para armazenar informações de um aluno:
• Nome, idade e curso.
• Depois, imprima os dados formatados
"""

dicionario = {
    "nome":"Diego",
    "idade": 35,
    "curso": "Sistemas de Informação"
}

print(f"Nome do aluno: {dicionario["nome"]}\nIdade: {dicionario.get("idade")}\nCurso: {dicionario.get("curso")}")