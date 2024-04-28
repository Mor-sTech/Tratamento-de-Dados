import numpy as np 
import pandas as pd 
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.styles import Alignment

df = pd.read_csv('imdbTop250.csv', low_memory=False)
df.isnull().sum()

#Creating a rev list to store gross income values
rev = []
for i in df['Gross'].values:
    rev.append(i)

#Removing comma from revenue  
rev_c=[]
for i in rev:
    if ',' in str(i):
        j=i.replace(',','')
        rev_c.append(j)
    else:
        rev_c.append(i)  
#Assigning the clean list as value for Gross Income column        
df['Gross']=rev_c

df['Gross']=df['Gross'].astype(float)
df.dtypes

##Votos
Votesn = []
for i in df['Votes']:
    Votesn.append(i)
Votesn  

v1 = []
for i in Votesn:
    if isinstance(i, str) and ',' in i:
        j=i.replace(',','')
        v1.append(j)
    else:
        v1.append(i)

df['Votes'] = v1

df['Votes']=df['Votes'].astype(float)

df['Votes']=df['Votes'].astype(int)

df.dtypes

# Renomeando várias colunas
df.rename(columns={'IMDBlink': 'IMDB-Titulo', 'Title': 'Titulo', 'Date': 'Ano', 'RunTime':'Duração', 'Genre':'Genero', 'Rating':'Avaliação', 'Score':'Aceitação', 'Votes':'Votos', 'Gross':'Faturamento', 'Director':'Diretor'}, inplace=True)
df.to_excel('imdbTop250_tratado.xlsx', index=False)

# Cria uma nova workbook
wb = Workbook()

# Selecionar a worksheet ativa
ws = wb.active

# Definir a largura das colunas
column_widths = {'A': 9, 'B': 9, 'C': 20, 'D': 40, 'E': 9, 'F': 9,'G': 30, 'H' : 9, 'I' : 9, 'J' : '15', 'K' : 15, 'L' : 25, 'M': 20, 'N':20, 'O':20, 'P': 20 } 

# Iterar sobre as colunas e ajustar a largura
for col, width in column_widths.items():
    ws.column_dimensions[col].width = width

# Converter DataFrame para o formato Excel e salvar no workbook
for r in dataframe_to_rows(df, index=False, header=True):
    ws.append(r)

# Centralizar e alinhar o texto no meio de todas as células
for row in ws.iter_rows(min_row=1, max_row=len(df) + 1, min_col=1, max_col=len(df.columns)):
    for cell in row:
        cell.alignment = Alignment(horizontal='center', vertical='center')

# Salve as alterações no excel
wb.save('imdbTop250_tratado.xlsx')