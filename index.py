import numpy as np 
import pandas as pd 

import seaborn as sns
import plotly.express as px
import plotly.offline as pyo
import matplotlib.pyplot as plt

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