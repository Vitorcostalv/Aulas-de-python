import csv
import json

# Escrevendo em um arquivo CSV
with open("dados.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Nome", "Idade", "Cidade"])
    writer.writerow(["Vitor", 20, "São Paulo"])
    writer.writerow(["San", 22, "Rio de Janeiro"])

# Lendo de um arquivo CSV
with open("dados.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Trabalhando com JSON
dados = {
    "nome": "Vitor",
    "idade": 20,
    "cidade": "São Paulo"
}

# Salvando como JSON
with open("dados.json", "w") as file:
    json.dump(dados, file, indent=4)

# Lendo de um arquivo JSON
with open("dados.json", "r") as file:
    conteudo = json.load(file)
    print(conteudo)
