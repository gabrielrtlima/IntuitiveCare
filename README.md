# PROCESSO SELETIVO IntuitiveCare

## __Teste 1 - WebScraping__

Neste teste o candidato deverá criar um código (em uma das linguagens mencionadas no fim desse email) que execute as tarefas de código abaixo.  

### __Tarefas de código__

- 1.1 - Acessar o site: <http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar>
- 1.2 - Buscar a versão mais recente do Padrão TISS (arquivo - padrao_tiss_componente_organizacional_201902.pdf);
- 1.3 - Baixar o componente organizacional;

### __Script__

- Para executar o script precisa das bibliotecas [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) e [Requests](https://pypi.org/project/requests/)
- O script foi pensado exclusivamente para essa atividade, ou seja, mesmo ele buscando automaticamente ele funcionará apenas nesse template visto que as marcações para buscar o pdf mais utilizado foi usado atraves das classes css (.alert-icon) e elementos do html (a[href*=".pdf"])

```python
for url_get_access in get_soup(url_base).select_one(".alert-icolink"):
    url_get_access = "http://www.ans.gov.br"+url_get_access['href']
    print('Acessando o {}'.format(url_get_access))

for url_get_download in get_soup_download(url_get_access).select('a[href*=".pdf"]'):
        url_get_download = 'http://www.ans.gov.br'+url_get_download['href']
        print('Iniciando o download no link: {}'.format(url_get_download))
```

- Por fim é só executar o script que ele baixará o pdf mais atualizado do site automaticamente na pasta *TESTE 1 - WebScraping*

## __Teste 2 - Transformação de dados__

Neste teste o candidato deverá criar um código (em uma das linguagens mencionadas no fim desse email) que execute as tarefas de código abaixo.

### __Tarefas do código__

- Extrair do pdf do teste 1 acima os dados dos Quadros 30,31,32 (Tabela de categoria do Padrão TISS);
- Salvar dados dessas tabelas em csvs;
- Zipar todos os csvs num arquivo "Teste_Intuitive_Care_{seu_nome}.zip".

### __Script__

- Foi usado o [tabula](https://pypi.org/project/tabula-py/), que além da instalação dele (*pip install tabula-py*), requer o [Java 8+](https://www.java.com/pt-BR/download/ie_manual.jsp?locale=pt_BR), para visualizar a leitura do pdf através do tabula.

- É um script bem simples de ser entendido, a única complexidade dele é entender como o tabula separa as tabelas, após isso só basta utilizar o for para automatizar as conversões.

- Após a execução do script ele salvará todos os arquivos na pasta *TESTE 2 - Transformação de dados*, separado por nomes de cada tabela convertida.