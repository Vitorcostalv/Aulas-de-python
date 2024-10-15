import re

# Verificando se uma string contém apenas dígitos
padrao = r"^\d+$"
texto = "12345"

if re.match(padrao, texto):
    print("A string contém apenas dígitos.")
else:
    print("A string não contém apenas dígitos.")

# Substituindo partes de uma string
texto = "O preço é R$100,00"
novo_texto = re.sub(r"R\$", "USD ", texto)
print("Texto atualizado:", novo_texto)
