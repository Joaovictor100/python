'''Sortear numero'''
from random import choice

lista = ['0', '1',
         '2', '3',
         '4', '5']

num = choice(lista)

print(71*'=')
print('\t\tQue número estou pensando')
print(71*'=')
num_pre = input('\t')

if num == num_pre:
    print('\033[1;34mParabéns! você acertou.\033[m')
elif num_pre in ('1', '2', '3', '4', '5'):
    print('Errou! tente novamente.\nNúmero certo:',num)
else:
    print(71*'-')
    print('\t\t\033[1;31mDigite um número de 0 a 5, número inválido\033[m')
    print(71*'-')
