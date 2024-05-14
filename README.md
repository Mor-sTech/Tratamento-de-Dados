# Tratamento-de-Dados
## Mors'Tech

## Seções:
- [Resumo](#resumo)
- [Destrinchando o código](#destrinchando-o-código---passo-a-passo)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Equipe](#equipe)



## Resumo
### Nesse repositório contem um código Python para tratamento do [dataset](https://www.kaggle.com/datasets/rajugc/imdb-top-250-movies-dataset) escolhido para o projeto de Database Application, o arquivo csv do dataset sem tratamento e o arquivo gerado pelo código Python utilizado, pós tratamento.

## Destrinchando o código - Passo a Passo

* Importa as bibliotecas necessárias: pandas, mysql.connector e create_engine do sqlalchemy.
* Carrega um arquivo CSV chamado 'IMDB_top_250_movies.csv' em um DataFrame do pandas chamado df_imdb.
* Exibe as primeiras linhas do DataFrame df_imdb usando o método head().
* Define uma string params que contém as informações de conexão para o banco de dados MySQL. Neste caso, está usando o usuário root, senha root, host localhost e a porta 3306, com o banco de dados chamado IMDB.
* Cria um objeto engine usando a função create_engine do SQLAlchemy, passando a string de conexão params como argumento. O parâmetro echo=True é usado para habilitar a exibição de mensagens de log que mostram as consultas SQL geradas pelo SQLAlchemy.
* Usa o método to_sql() do pandas DataFrame para inserir os dados do DataFrame df_imdb na tabela imdb_stage no banco de dados MySQL especificado pela conexão engine. O parâmetro if_exists='replace' especifica que se a tabela imdb_stage já existir, ela será substituída pelos dados do DataFrame. O parâmetro index=False indica que os índices do DataFrame não devem ser incluídos como coluna no banco de dados.

## Tecnologias utilizadas

* Visual Studio Code (ou um editor de código semelhante)
* Docker
* MYSQL Workbench
* Jupyter Notebook
* Python
* Biblioteca Pandas
* Biblioteca Mysql Connector
* Biblioteca SQLAlchemy



## Equipe

* Jessica Nascimento Pessoa da Silva - 01717533
* João Guilherme Caetano dos Santos - 01481382
* João Victor Mendonça da Silva - 01480878
* Paulo Vinícius Feliciano de Souza - 01618133
* Rosilene da Silva Lima - 01619051
