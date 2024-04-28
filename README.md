# Tratamento-de-Dados
## Mors'Tech

## Seções:
- [Resumo](#Resumo)
- [Destrinchando o código](#Destrinchando-o-código)
- [Equipe](#equipe)



## Resumo
### Nesse repositório contem um código Python para tratamento do [dataset](https://www.kaggle.com/datasets/rajugc/imdb-top-250-movies-dataset) escolhido para o projeto de Database Application, o arquivo csv do dataset sem tratamento e o arquivo gerado pelo código Python utilizado, pós tratamento.

## Destrinchando o código - Passo a Passo

* Lê um arquivo CSV chamado 'IMDB Top 250 Movies.csv' e carrega os dados em um DataFrame df.
* Remove valores nulos do DataFrame.
* Cria uma lista chamada rev para armazenar os valores da coluna 'box_office'.
* Remove vírgulas dos valores na lista rev.
* Lida com a parte dos votos da coluna 'rating' do DataFrame, removendo vírgulas dos valores e convertendo-os para o tipo float.
* Define uma função format_accounting_number para formatar os valores em formato de número contábil do Excel.
* Aplica a formatação aos valores das colunas 'box_office' e 'budget'.
* Renomeia várias colunas do DataFrame df.
* Cria um novo arquivo Excel e uma planilha ativa.
* Define a largura das colunas da planilha.
* Converte o DataFrame para o formato Excel e o salva na planilha.
* Aplica o formato de número contábil às células da coluna 'box_office'.
* Centraliza e alinha o texto no meio de todas as células da planilha.
* Cria bordas finas em todas as células da planilha.
* Aplica estilo de fonte negrito à linha 1 da planilha.
* Aplica a cor de preenchimento à linha 1 da planilha.
* Salva as alterações no arquivo Excel.

## Equipe

* Jessica Nascimento Pessoa da Silva - 01717533
* João Guilherme Caetano dos Santos - 01481382
* João Victor Mendonça da Silva - 01480878
* Paulo Vinícius Feliciano de Souza - 01618133
* Rosilene da Silva Lima - 01619051