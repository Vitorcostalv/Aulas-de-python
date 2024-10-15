# Arquivo "meu_modulo.py"
def saudacao(nome):
    return f"Olá, {nome}!"

# Importando o módulo
import meu_modulo

print(meu_modulo.saudacao("Vitor"))

# Estrutura de pacotes (diretórios com arquivos __init__.py)
# pasta_pacote/
# ├── __init__.py
# └── modulo1.py
