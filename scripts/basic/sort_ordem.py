'''Sortear ordem de número'''
from random import shuffle

NUM = 0
# Contador

n1 = input('Primeira pessoa: ').strip().title()
n2 = input('Segunda pessoa: ').strip().title()
n3 = input('Terceira pessoa: ').strip().title()
n4 = input('Quarta pessoa: ').strip().title()
n5 = input('Quita pessoa: ').strip().title()

# Sorteio
lista = [n1, n2,
         n3, n4,
         n5]
shuffle(lista)

# Mostre
print('A ordem é: ')
for element in lista:
    NUM = NUM+1
    print(f'\t{NUM} {element}')
