# Tratamento de Exceções em Python
# ---------------------------------

# Exemplo de Valor inválido para uma operação (int("abc"))
try:
    numero = int("abc")   # Vai gerar erro
except ValueError:
    print("Erro: valor inválido!")
finally:
    print("Execução finalizada.")

# Exemplo de uso com múltiplas exceções
try:
    x = int("abc")
    y = 10 / 1
except ValueError:
    print("Valor inválido")
except ZeroDivisionError:
    print("Divisão por zero")
except Exception as e:
    print(f"Outro erro: {e}")
finally:
    print("Comando executado sempre!")

