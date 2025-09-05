'''previsao do dolar'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Carregando o CSV
arquivo = pd.read_csv('dados.csv')

# Convertendo a coluna 'data' para datetime
arquivo['data'] = pd.to_datetime(arquivo['data'], format="%d/%m/%Y")

# Criando colunas separadas para dia, mês e ano
arquivo['ano'] = arquivo['data'].dt.year
arquivo['mes'] = arquivo['data'].dt.month
arquivo['dia'] = arquivo['data'].dt.day

x = arquivo.drop(['dolares', 'data'], axis=1)
y = arquivo['dolares']

x_treino, x_test, y_treino, y_test = train_test_split(x, y, test_size=0.3)

modelo = RandomForestRegressor()
modelo.fit(x_treino, y_treino)

resultado = modelo.score(x_test, y_test)

print(resultado)
print('Previsão do dólar')

dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

dados_previsao = pd.DataFrame({
    'ano': [ano],
    'mes': [mes],
    'dia': [dia]
})


previsao = modelo.predict(dados_previsao)

print(f'Em {ano}/{mes}/{dia} o dólar estará {previsao[0]} U$')

