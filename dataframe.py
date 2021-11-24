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

vendas_df = pd.read_excel("Vendas.xlsx")
print(vendas_df)
print('----------------------------------')

print(vendas_df.head())
print('----------------------------------')

print(vendas_df.shape)
print('----------------------------------')

print(vendas_df.describe())
print('----------------------------------')

produtos = vendas_df[['Produto']]
print(produtos)

