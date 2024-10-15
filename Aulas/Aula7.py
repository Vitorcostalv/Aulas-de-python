# Aula 7: Dicionários
# Criando um dicionário com informações de uma pessoa
pessoa = {
    "nome": "Vitor",
    "idade": 20,
    "cidade": "São Paulo"
}

# Acessando valores no dicionário
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])

# Adicionando um novo par chave-valor
pessoa["altura"] = 1.75
print("Dicionário atualizado:", pessoa)
