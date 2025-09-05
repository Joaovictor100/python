'''Sorteio'''
from random import choice

# Ler nomes
n1 = input('Primeiro nome: ').strip().title()
n2 = input('Segundo nome: ').strip().title()
n3 = input('Terceiro nome: ').strip().title()
n4 = input('Quarto nome: ').strip().title()
n5 = input('Quinto nome: ').strip().title()

# Lista dos nomes
lista = [
    n1, n2,
    n3, n4,
    n5]

# Sorteando em Mostrando o resultado
print(71*'=')
print('    A pessoa sorteada é:',choice(lista))
print(71*'=')
