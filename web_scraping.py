import os
import requests
import zipfile
from bs4 import BeautifulSoup

# url do site onde os anexos estão disponíveis
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"


#Selecionar pasta para salvar os arquivos baixados
download_path = "downloads"
os.makedirs(download_path, exist_ok=True)

# Faz requisição HTTP para obter o html da página
response = requests.get(url)
if response.status_code != 200:
    print('Erro ao acessar o site!')
    exit()

#Analisar o HTML com BeatifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Procurar os links para os anexos
anexos = []

for link in soup.find_all("a", href=True):
    if "Anexo I" in link.text or "Anexo II" in link.text:
        if link["href"].endswith(".pdf"):
            anexos.append(link["href"])

#Se caso não encontrar links, interrompera
if not anexos:
    print("Nenhum anexo foi encontrado!")
    exit()

# Baxando os arquivos PDFs encontrados
arquivos_baixados = []
for idx, anexo_url in enumerate(anexos, start=1):
    anexo_nome = f"Anexo_{idx}.pdf"
    anexo_path = os.path.join(download_path, anexo_nome)

    # Fazer o download do arquivo
    anexo_response = requests.get(anexo_url)
    with open(anexo_path, 'wb') as file:
        file.write(anexo_response.content)

    arquivos_baixados.append(anexo_path)
    print(f"Baixados: {anexo_nome}")

# Compactando os arquivos em ZIP 
zip_filename = "anexos_compactados.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for arquivo in arquivos_baixados:
        zipf.write(arquivo, os.path.basename(arquivo))

print(f"Compactação foi concluída com sucesso> {zip_filename}")