# Aula 5: Funções
def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo.")

# Chamando a função
saudacao("Vitor")

# Função que retorna o quadrado de um número
def quadrado(numero):
    return numero ** 2

resultado = quadrado(4)
print("O quadrado de 4 é:", resultado)
