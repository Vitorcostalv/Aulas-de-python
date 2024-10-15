import requests
from bs4 import BeautifulSoup

# Requisição para obter o conteúdo de uma página
url = "https://example.com"
resposta = requests.get(url)

# Analisando o conteúdo HTML
soup = BeautifulSoup(resposta.content, "html.parser")

# Extraindo e exibindo os títulos de todas as tags <h1>
titulos = soup.find_all("h1")
for titulo in titulos:
    print("Título:", titulo.text)
