import random
import string

def gerar_senha(tamanho=8):
    # Define os caracteres possíveis: letras maiúsculas, minúsculas e dígitos
    caracteres = string.ascii_letters + string.digits
    # Gera a senha aleatória
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Gera uma senha de até 8 caracteres
senha_gerada = gerar_senha()
print("Senha gerada:", senha_gerada)
