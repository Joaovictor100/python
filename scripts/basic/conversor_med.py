'''Conversor de medidas'''

try:
    km = float(input('Digite um numero em km: '))
except ValueError:
    print('Erro de digitaçao tente novamente')

# Conversão
hec = km*10
dec = km*100
m = km*1000
cm = km*100000
mm = km*1000000
ml = km*1000000000
n = km* 1000000000000

# Imprimir
print(f'''
km:{km}
hectometro:{hec}
decametros:{dec}
metros:{m}
centimetros:{cm}
milimetros:{mm}
micro: {ml}
nanometros:{n}''')
