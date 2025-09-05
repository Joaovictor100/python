'''
João Victor Soares Toledo Silva

===================================================================
Project Machine Learning classification of numbers
===================================================================

22/12/2023

'''

import numpy as np

class BinaryClassifier:
    '''
    Essa classe cria um modelo, esse modelo é treinado identificando padrões,
    e logo depois faz a classificação de 1 ou 0
    '''
    def __init__(self):
        self.pesos = None
        
    def sigmoid(self, x):
        '''
        Essa função serve para transformar qualquer número em um intervalo entre 1 e 0,
        por ele conter casas decimas pode ser mais preciso em calculos,
        diferentes dos degraus, o sigmoid é bem preciso.
        '''
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, output):
        '''
        A função derivada da sigmoid ajuda a regular os pesos da machine learning
        ela recebe a saida da multiplicação de pesos entre dados de entrada.
        '''
        return output * (1 - output)
    
    def fit(self, X, y, epochs=10000):
        '''
        Tem o objetivo de treinar a machine learning e com parâmetros, regular os pesos:
        X: entrada de dados para a treino: float ou int;
        y: rotulos, resultados, ajuda a calcular o erro: int;
        epochs: número de épocas de treinamento da machine learning: int
        '''
        dados_entrada = X
        dados_rotulos = y
        
        np.random.seed(1)
        
        self.pesos = np.random.random((len(dados_entrada[0]), 1)) - 1
        for epoch in range(epochs):
            output = self.sigmoid(np.dot(dados_entrada, self.pesos))
            
            error = dados_rotulos - output
            ajuste = error * self.sigmoid_derivative(output)
            
            self.pesos += np.dot(dados_entrada.T, ajuste)
    def predict(self, X):
        '''
        Essa função vai retornar a previsão de novos dados:
        X: dados para serem previstos: int or float;
        retornar a classificação 0 ou 1.
        '''
        result = self.sigmoid(np.dot(X, self.pesos))
        return np.where(result >= 0.5, np.ceil(result), np.floor(result))
    
    def score(self,X, y):
        result = self.sigmoid(np.dot(X, self.pesos))
        result_arredondado = np.where(result >= 0.5, np.ceil(result), np.floor(result))
        numeros_corretos = np.count_nonzero(result_arredondado == y)
        
        precisao = numeros_corretos / len(X)
        return precisao

# usando o modelo
modelo = BinaryClassifier()

X = np.array([[0, 0, 1],
              [1, 1, 1],
              [0, 1, 1],
              [1, 0, 0],
              [1, 0, 0],
              [0, 1, 0],
              [0, 0, 1],
              [1, 1, 0],
              [0, 1, 0],
              [1, 0, 1],
              [1, 0, 1],
              [0, 1, 1],
              [1, 1, 1],
              [0, 0, 0],
              [0, 1, 1]])

y = np.array([[1,1,1,0,0,0,1,0,0,1,1,1,1,0,1]]).T # transposta

modelo.fit(X, y, epochs=50000)

X_test = np.array([[0, 0, 0],
              [1, 0, 0],
              [1, 0, 1],
              [1, 0, 1],
              [0, 1, 0]])
              
y_test = np.array([[0,0,1,1,0]]).T # transposta

print('Precisão', modelo.score(X_test, y_test))
print()
