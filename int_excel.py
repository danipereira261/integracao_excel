import pandas as pd

tabela = pd.read_excel("Produtos.xlsx")
print(tabela)

# atualizar o multiplicador
tabela.loc[tabela["Tipo"]=="Serviço", "Multiplicador Imposto"] = 1.5

# fazer a conta do Preço Base Reais
tabela["Preço Base Reais"] = tabela["Multiplicador Imposto"] * tabela["Preço Base Original"]

# salvar o arquivo em excel sem o indice
tabela.to_excel("ProdutosPandas.xlsx", index=False)