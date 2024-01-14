'''Calculo da hipotenusa'''
b = float(input('Comprimento do cateto oposto: '))
c = float(input('Comprimento do cateto adjecente: '))

# Calculo **(1/2) seria para calcular uma raiz quadrada
a = (b**2+c**2)**(1/2)

# Mostre
print(f'\tA hipotenusa medi: {a:.2f}')
