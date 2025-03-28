import pandas as pd
import pdfplumber
import zipfile
import os

# Função que irá extrair os dados do PDF
def extrair_dados_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        todas_as_paginas = []
        for pagina in pdf.pages:
            texto = pagina.extract_text()
            todas_as_paginas.append(texto)
    return "\n".join(todas_as_paginas)

# Método para salvar os dados em CSV usando a biblioteca Pandas
def salvar_em_csv(dados, arquivo_csv):
    df = pd.DataFrame(dados) # Criando um DataFrame com os dados extrídos anteriormente
    # Salvando como o DataFrame csv
    df.to_csv(arquivo_csv, index=False, encoding='utf-8')

# Método para compactar o csv em um arquivo ZIP
def compactar_em_zip(arquivo_csv, nome_zip):
    with zipfile.ZipFile(nome_zip, 'w') as zipf:
        zipf.write(arquivo_csv, os.path.basename(arquivo_csv))

# Função para substituir as abreviações pelas descrições completas
def substituir_abreviacoes(df):
    legenda_abreviacoes = {
        "OD" : "Óptica Domiciliar",
        "AMB" : "Ambulatório"
    }
    # Substituindo as abreviações pelas descrições completas em todas as colunas
    for colouna in df.columns:
        df[colouna] = df[colouna].replace(legenda_abreviacoes)

    return df

# Principal Método
def processo():
    #caminho do PDF (Anexo I)
    pdf_path = "//workspaces//Testes-de-Nivelamento//downloads//Anexo_1.pdf"

    # Extraindo os dados do PDF
    texto_pdf = extrair_dados_pdf(pdf_path)

    #Dividindo o texto extraído por linha
    linhas = texto_pdf.split("\n")

    #Filtrando as linhas da tabela
    dados_tabela = []
    for linha in linhas:
        if linha.strip(): # ingnora linhas vazias
            dados_tabela.append(linha.split())  # Dividindo por espaços para extrair colunas

    #Criar o DataFrame
    df = pd.DataFrame(dados_tabela)

    #Subistituir as abreviações nas colunas
    df = substituir_abreviacoes(df)

    # Salvar todos os dados no arquivo CSV
    arquivo_csv = "Rol_de_Procedimentos.pdf"
    salvar_em_csv(df, arquivo_csv)

    # Por último compactar o CSV em um arquivo ZIP
    nome_zip = "Teste_Marlon.zip"
    compactar_em_zip(arquivo_csv, nome_zip)
    print(f"Processo concluido com sucesso! Aquivo ZIP gerado: {nome_zip}")

#Executando o processo
processo()