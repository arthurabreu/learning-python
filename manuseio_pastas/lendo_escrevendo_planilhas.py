from pathlib import Path
import pandas as pd
import openpyxl

pasta_atual = Path(__file__).parent

# lendo tabelas com DataFrame
# planilha_teste = pd.read_excel(pasta_atual / 'planilha_teste.xlsx', engine='openpyxl')
# print(planilha_teste)

# lendo aba específica
planilha_teste_aba = pd.read_excel(pasta_atual / 'planilha_teste.xlsx', sheet_name='Planilha1')
print(planilha_teste_aba)

# lendo várias abas
planilhas = pd.read_excel(pasta_atual / 'planilha_teste.xlsx', sheet_name=None, engine='openpyxl')
for nome_aba, df in planilhas.items():
    print(f"Aba: {nome_aba}")
    print(df)