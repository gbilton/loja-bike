import pandas as pd

produtos = pd.read_excel('tabelas.xlsx', sheet_name='Produtos')
clientes = pd.read_excel('tabelas.xlsx', sheet_name='Clientes')
vendas = pd.read_excel('tabelas.xlsx', sheet_name='Vendas')
