# Testes-de-Nivelamento
# Web Scraping - Versão 1.1
O objetivo desse script de web scraping é fazer o download de arquivos PDF (Anexo I e Anexo II) disponíveis em um site do Governo. A versão 1.1 foi feita para baixar apenas os arquivos PDF, já que a versão anterior estava baixando 3 arquivos desnecessários.

Como o código funciona:
Requisição HTTP: O script começa fazendo uma requisição HTTP para obter o HTML da página que contém os links para os arquivos PDF (Anexo I e Anexo II).

Análise do HTML: Com a biblioteca BeautifulSoup, o código analisa o HTML da página e busca por links (<a>) que contêm os textos "Anexo I" ou "Anexo II", e filtra apenas os links que terminam com .pdf.

Download dos PDFs: Para cada link encontrado, o script faz o download do arquivo PDF e o salva em uma pasta chamada downloads.

Compactação: Após o download, todos os arquivos PDF são compactados em um arquivo ZIP chamado "anexos_compactados.zip".

# Transformação de Dados
Esse código tem o objetivo de extrair dados de um PDF (Anexo I), estruturar esses dados em um DataFrame, substituir abreviações por descrições completas e, por fim, salvar esses dados em um arquivo CSV. Em seguida, o arquivo CSV é compactado em um arquivo ZIP.

Como o código funciona:
Extração dos dados do PDF: O script usa a biblioteca pdfplumber para abrir e ler todas as páginas de um PDF. Ele extrai o texto de todas as páginas e os junta em uma string.

Filtragem e Processamento dos Dados: O texto extraído é dividido em linhas e, em seguida, é feito o processamento para separar as colunas usando espaços. Apenas as linhas com dados são mantidas.

Substituição de Abreviações: O script substitui as abreviações nas colunas do DataFrame por descrições mais completas. Por exemplo, "OD" é substituído por "Óptica Domiciliar" e "AMB" por "Ambulatório".

Salvamento em CSV: Com a biblioteca pandas, o script organiza os dados em um DataFrame e salva esse DataFrame em um arquivo CSV.

Compactação em ZIP: Após salvar o CSV, o arquivo é compactado em um arquivo ZIP com o nome "Teste_Marlon.zip".

# Esses dois scripts permitem:

Baixar automaticamente os arquivos PDF (Anexo I e Anexo II) de um site específico e compactá-los em um arquivo ZIP.
Extrair e processar dados de um PDF, substituindo abreviações por descrições completas, e salvar esses dados como um arquivo CSV, que também é compactado em um arquivo ZIP.
Ambos os scripts fazem parte de um fluxo de automação de dados desde a coleta (web scraping) até a organização e armazenamento (transformação de dados).
