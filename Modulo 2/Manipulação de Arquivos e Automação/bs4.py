import requests
from bs4 import BeautifulSoup

url = "https://sp.senai.br/unidade/santanadeparnaiba/"  # URL alvo

# 1. Fazer requisição HTTP
response = requests.get(url)
response.raise_for_status()  # Garante que a página foi acessada com sucesso

# 2. Criar objeto BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# 3. Encontrar a tag <h1>
h1_tag = soup.find("h1")  # Retorna a primeira ocorrência
# Alternativa: buscar todas com soup.find_all("h1")

# 4. Extrair o texto, se existir
if h1_tag:
    texto = h1_tag.get_text(strip=True)
    novo = "melhor do mundo"
    print("Conteúdo da tag <h1>:", texto + novo)
else:
    print("Nenhuma tag <h1> encontrada nesta página.")
