'''Machine Learn'''
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier

#abrindo o arquivo csv
arquivo = read_csv("dados.csv")
arquivo.head()

#substituindo red por 0 e white por 1
arquivo['style'] = arquivo['style'].replace('red', 0)
arquivo['style'] = arquivo['style'].replace('white', 1)

#separar variável alvo de preditoras
y = arquivo['style']
x = arquivo.drop('style', axis=1)

#treinando machine
x_treino, x_test, y_treino, y_test= train_test_split(x, y, test_size = 0.3)

#Criação do modelo:
modelo = ExtraTreesClassifier(n_estimators=100)
modelo.fit(x_treino, y_treino)

#Imprimindo resultados:
resultado = modelo.score(x_test, y_test)
print("Resultado do teste:", resultado)
print(y_test[480:403])
print(x_test[400:403])
previsoes = modelo.predict(x_test[400:403])
print(previsoes)

