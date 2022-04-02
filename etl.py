import pandas as pd

df = pd.read_csv('/home/j-paulo/PROGRAMMER/projeto_ETL/ocorrencia.csv', sep=',', index_col=0, parse_dates=[6])

print(df)
print(df.dtypes)

