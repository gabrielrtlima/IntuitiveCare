from bs4 import BeautifulSoup as bs
import requests

domain = 'http://www.ans.gov.br'
url_base = 'http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar'

def get_soup(url):
    return bs(requests.get(url_base).text, 'html.parser') 

for url_get_access in get_soup(url_base).select_one(".alert-icolink"):
    url_get_access = "http://www.ans.gov.br"+url_get_access['href']
    print('Acessando o {}'.format(url_get_access))

    def get_soup_download(url):
        return bs(requests.get(url_get_access).text,'html.parser')
     
    for url_get_download in get_soup_download(url_get_access).select('a[href*=".pdf"]'):
        url_get_download = 'http://www.ans.gov.br'+url_get_download['href']
        print('Iniciando o download no link: {}'.format(url_get_download))

    def downloadFile(url, address):
        response = requests.get(url)
        with open(address,'wb') as newFile:
            newFile.write(response.content)

if __name__ == '__main__':     
    downloadFile(url_get_download, 'TESTE 1 - WebScraping\IntuitiveCare.pdf')
    print('Download concluido!')