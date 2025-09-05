'''
Modelo de Regressão Linear para apredizado de máquina
'''

import numpy as np
from pandas import DataFrame

class LinearRegression:
    '''
    Modelo Regressão Linear.
    normalize: normaliza os dados para entra no modelo
    fit: treina os dados, ajusta os pesos com gradiente
    predict: preve os dados com o modelo já treinado
    '''
    
    def __init__(self, learning_rate=0.01, epochs=7000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weight = None
        self.error = None
        self.mean = None # Média
        self.std = None # Desvio padrão

    def normalize(self, data):
        '''
        Normaliza od dados do modelo para que não de overflow
        '''
        self.mean = np.mean(data, axis=0)
        self.std = np.std(data, axis=0)
        normalized_data = (data - self.mean) / self.std
        return normalized_data

    def fit(self, trein_x, trein_y):
        '''
        Esse método ira treinar o modelo
        '''
        trein_x = np.c_[np.ones(trein_x.shape[0]), self.normalize(trein_x)]
        self.weight = np.random.rand(trein_x.shape[1])

        for _ in range(self.epochs):
            output = np.dot(trein_x, self.weight)
            self.error = output - trein_y

            gradients = np.dot(trein_x.T, self.error) / len(trein_y)

            self.weight -= self.learning_rate * gradients

    def predict(self, predict_x):
        '''
        Com os pesos já ajustados e machine learning treinada, esse.método ira prever dados.
        '''
        predict_x = np.c_[np.ones(predict_x.shape[0]), (predict_x - self.mean) / self.std]
        return np.dot(predict_x, self.weight)

    def score(self, score_x, score_y):
        '''
        Esse método mostra a precisão do modelo, precisão, exemplo 1.0 modelo perfeito.
        '''
        score_x = np.c_[np.ones(score_x.shape[0]), (score_x - self.mean) / self.std]
        bool_array = score_y == np.around(np.dot(score_x, self.weight))
        number_true = np.sum(bool_array)
        precision = number_true / len(bool_array)
        return precision

X = np.array([[1, 2], [2, 3],
              [3, 4], [4, 5],
              [5, 6], [7, 8],
              [5, 6], [23, 24],
              [45, 46], [67, 68],
              [89, 90], [22, 23]])

y = np.array([3, 4, 5, 6, 7, 9, 7, 25, 47, 69, 91, 24])

model = LinearRegression(epochs=5000)
model.fit(X, y)

data_predict = np.array([[6, 7], [7, 8]])
predict_y = model.predict(data_predict)

test_x = np.array([[20, 21], [45, 46], [78, 79], [12, 13]])
test_y = np.array([22, 47, 80, 14])

data_test = model.score(test_x, test_y)

print('Resultado da previsão:', predict_y)
print('Dados Reais\n', data_predict)
print('Precisão do modelo', data_test)
