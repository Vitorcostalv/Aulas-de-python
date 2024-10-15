# Aula 8: Leitura e Escrita de Arquivos
# Criando e escrevendo em um arquivo
with open("arquivo.txt", "w") as arquivo:
    arquivo.write("Esta é a primeira linha.\n")
    arquivo.write("Esta é a segunda linha.\n")

# Lendo o conteúdo do arquivo
with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:\n", conteudo)
