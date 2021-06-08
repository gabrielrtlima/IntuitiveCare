from bs4 import BeautifulSoup as bs
import requests

#dominio
domain = 'http://www.ans.gov.br'
#url inicial de acesso
urlBase = 'http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar'


soupAccess = bs(requests.get(urlBase).text, 'html.parser') 

#buscando o link da página de download referente ao mais recente por classe css (.alert-icolink)
for a in soupAccess.select_one(".alert-icolink"):
    urlGetAccess = "http://www.ans.gov.br"+a['href']
    print('Acessando o {}'.format(urlGetAccess))

soupGetDownload = bs(requests.get(urlGetAccess).text,'html.parser')

#buscando o url do download para o pdf utilizando a marcação (a) e filtrando o link com final .pdf [href*=".pdf"]
for urlGetDownload in soupGetDownload.select('a[href*=".pdf"]'):
    urlGetDownload = 'http://www.ans.gov.br'+urlGetDownload['href']
    print('Iniciando o download no link: {}'.format(urlGetDownload))

#função para download do arquivo
def downloadFile(url, address):
    response = requests.get(url)
    with open(address,'wb') as newFile:
        newFile.write(response.content)
    
downloadFile(urlGetDownload, 'IntuitiveCare.pdf')
print('Download concluido!')