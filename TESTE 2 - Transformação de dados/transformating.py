import tabula 

pdf_path = 'TESTE 2 - Transformação de dados\IntuitiveCare.pdf'
dfs = tabula.read_pdf(pdf_path, pages="79-85")

for i in range(0,8):
    
    if i == 0:
        dfs[i].to_csv('TESTE 2 - Transformação de dados\Tipo_Do_Mandante.csv', encoding='utf-8')
        i += 1
        print('Convertendo a tabela de transformação de dados...')
    elif i <= 6:
        dfs[i].to_csv('TESTE 2 - Transformação de dados\Categoria_Do_Padrao1.{}.csv'.format(i-1), encoding='utf-8')
        i += 1
        print('Convertendo a tabela de categoria do padrão parte 1.{}...'.format(i-1))
    else:
        dfs[i].to_csv('TESTE 2 - Transformação de dados\Tipo_De_Solicitacao.csv', encoding='utf-8')
        i += 1
        print('Convertendo a tabela de transformação de dados...\nFIM!')