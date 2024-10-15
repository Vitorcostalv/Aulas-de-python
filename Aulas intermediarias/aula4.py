# Definindo uma exceção personalizada
class ErroPersonalizado(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

# Usando a exceção personalizada
def dividir(a, b):
    if b == 0:
        raise ErroPersonalizado("Divisão por zero não é permitida.")
    return a / b

try:
    resultado = dividir(10, 0)
    print("Resultado:", resultado)
except ErroPersonalizado as e:
    print("Erro:", e)
