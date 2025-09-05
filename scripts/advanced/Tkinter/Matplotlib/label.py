import matplotlib.pyplot as plt
x = [0,2,3,4]
y = [0,4,6,8]
x2 = [0,2,3,4]
y2 = [0,3,4,6]

plt.plot(x,y, color='#00f', label='Joao Victor') # adicionar legenda pelo label, define o nome dele
plt.plot(x2,y2, color='#f00', label='outro dev')
plt.xlabel('Tempo (anos)') # nome para o eixo x
plt.ylabel('Conhecimento') # nome para o eixo y
plt.legend() # adicionar os nomes
plt.title('Melhor em programação') # titulo do grafico
plt.show()