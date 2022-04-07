import pandas as pd 
import pandera as pa # nécessario para montar o esquema do DF

df = pd.read_csv('/home/j-paulo/PROGRAMMER/projeto_ETL/ocorrencia.csv', sep=',', parse_dates=['ocorrencia_dia'], dayfirst=True)

schema = pa.DataFrameSchema(
        columns = {
            'ocorrencia_dia':pa.Column(pa.DateTime, nullable=True), # ignora espaços nulos
            'codigo_ocorrencia':pa.Column(pa.Int),
            'ocorrencia_cidade':pa.Column(pa.String)
                                            }
            )

# df.codigo_ocorrencia.is_unique --> verifica se o valor naquela coluna é unica
# df.set_index('codigo_ocorrencia', inplace=True) --> Para mudar o índice
# df.reset_index(drop=True, inplace=True) --> Voltando ao indice original
# df.loc[linha, coluna] --> Para alteração ou visualização
# df.loc[df.ocorrencia_dia == '2012-01-05', ['ocorrencia_dia']] = '2012-02-05' --> Pesquisa uma data e a substitui por outra.
# df.loc[df.ocorrencia_dia == '', ['ocorrencia_dia']] = pd.NA --> Padrão para dados não informados no pandas.
# df.replace([lista a ser alterada], pd.NA, inplace=True) --> procura os valores informados na lista e os converte para NA.
# df.isna().sum() ou df.isnull().sum()--> Mostra a quantidade de NAs por coluna
# df.fillna('o que vai no lugar do na', inplace=True) --> Para substituir os NAs.
# df.drop(['lista de colunas a serem excluidas'], axis=1, inplace=True ) --> Excluir colunas no DF.
# df.dropna() --> Exclui todos os NAs
# filtro = df.'nome da coluna' > 10 --> Cria um filtro para numeros maiores que 10 na coluna
# df.loc[filtro] --> localiza esse filtro
# df.groupby(['coluna1', 'coluna2']).size() --> agrupa pelas colunas escolinhidas fazendo a ontagem das ocorrências.





schema.validate(df) # validação do esquema


print(df.dtypes)

