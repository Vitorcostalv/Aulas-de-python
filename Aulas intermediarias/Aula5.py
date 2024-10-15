# List comprehensions
numeros = [1, 2, 3, 4, 5]
quadrados = [n ** 2 for n in numeros]
print("Quadrados:", quadrados)

# Geradores
def gerador_de_numeros(maximo):
    numero = 1
    while numero <= maximo:
        yield numero
        numero += 1

for numero in gerador_de_numeros(5):
    print("Gerado:", numero)
