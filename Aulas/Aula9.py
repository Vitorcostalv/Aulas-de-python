# Aula 9: Tratamento de Exceções
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print("Resultado:", resultado)
except ValueError:
    print("Por favor, digite um número válido.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
finally:
    print("Fim do bloco de exceções.")
