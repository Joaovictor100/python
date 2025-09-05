'''Machine Learn'''
from pandas import read_csv, DataFrame
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier

#abrindo o arquivo csv
arquivo = read_csv("dados.csv")
arquivo.head()

# separar variável alvo de preditoras
y = arquivo['qualidade']
x = arquivo[['velocidade', 'torque']]

#treinando machine
x_treino, x_test, y_treino, y_test= train_test_split(x, y, test_size = 0.3, random_state=20)

#Criação do modelo:
modelo = ExtraTreesClassifier(n_estimators=100)
modelo.fit(x_treino, y_treino)

#Imprimindo resultados:
resultado = modelo.score(x_test, y_test)

# Dados de previsão
velocidade = int(input('Digite a velocidade do carro em Km/h: '))
torque = int(input('Digite o torque do carro em Nn: '))

# criar um dataframe para as previsoes terem rotulos, e não haver reclamações
df = DataFrame({
    'velocidade': [velocidade],
    'torque': [torque],
})

# Supondo que predict() retorna uma lista ou array
previsoes = modelo.predict(df)

# Mapear os valores preditos para rótulos desejados
mapeamento_rotulos = {1: 'ruim', 2: 'bom', 3: 'muito bom'}
previsoes_rotuladas = [mapeamento_rotulos.get(valor, valor) for valor in previsoes]

print('Seu carro é', str(previsoes_rotuladas[0]))
