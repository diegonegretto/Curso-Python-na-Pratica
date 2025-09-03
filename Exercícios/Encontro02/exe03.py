"""
3. Lista – Notas de Alunos
Crie uma lista com as notas [7.5, 8.0, 6.0, 9.5, 10.0].
• Adicione uma nova nota à lista;
• Remova a menor nota;
• Mostre a média final.
"""

notas = [7.5,8.0,6.0,9.5,10.0]

#Adicionando uma nova nota à lista
notas.append(8.5)
# Removendo a menor nota
notas.remove(min(notas))
# Calculando a média final
media = sum(notas) / len(notas)

# Mostrando resultados
print("Notas após as alterações:", notas)
print("Média final:", media)