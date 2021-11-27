import pandas as pd

venda = {'data': ['15/02/2021', '16/02/2021'],
         'valor': [500, 300],
         'produto': ['feijao', 'arroz'],
         'qtde': [50, 70]
         }
vendas_df = pd.DataFrame(venda)
print(venda)
print(vendas_df)
print('----------------------------------')
##
vendas_df = pd.read_excel("Vendas.xlsx")
print(vendas_df)
print('----------------------------------')
##
print(vendas_df.head())
print('----------------------------------')

print(vendas_df.shape)
print('----------------------------------')

print(vendas_df.describe())
print('----------------------------------')

produtos = vendas_df[['Produto']]
print(produtos)
print('----------------------------------')

produtos = vendas_df[['Produto', 'ID Loja']]
print(produtos)
print('----------------------------------')

print(vendas_df.loc[1])
print('----------------------------------')

# Pegar uma linha
print(vendas_df.loc[1:5])
print('----------------------------------')

# Pegar linhas que correspondem a uma condição
print(vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping'])
print('----------------------------------')

# Filtrar linhas e colunas
vendas_norte_shopping_df = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping', ['ID Loja', 'Produto', 'Quantidade']]
print('----------------------------------')

# Pegar um valor especifico
print(vendas_df.loc[1: 'Produto'])

# Adicionar uma coluna a partir de uma que ja exista
vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.05
print(vendas_df)

# criar uma coluna com valor padrão
##
vendas_df.loc[:, 'Imposto'] = 0
print(vendas_df)
##








