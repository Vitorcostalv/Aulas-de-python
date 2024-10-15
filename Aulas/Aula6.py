# Aula 6: Manipulação de Strings
texto = "Hello, World!"

# Convertendo para maiúsculas e minúsculas
print(texto.upper())
print(texto.lower())

# Fatiando strings
print("Primeiros 5 caracteres:", texto[:5])
print("Últimos 6 caracteres:", texto[-6:])

# Substituindo palavras
novo_texto = texto.replace("World", "Python")
print("Texto substituído:", novo_texto)
