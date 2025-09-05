'''Arrendondamento'''
from math import floor
from math import ceil
OP = ''
ERRO = True
try:
    N1 = float(input('Digite um numero real: '))
except ValueError:
    print('Número digitado errado, tente novamente')
    ERRO = False
while OP != '1' or OP != '2':
    if ERRO is False:
        break
    OP = input('''Escolha a opção
    1. Arredondar o número para baixo
    2. Arredondar o número para cima
    \t''').strip()
    if OP == '1':
        num_arren = floor(N1)
        print(f'O número {N1} arredondado para baixo fica {num_arren}')
    elif OP == '2':
        num_arren = ceil(N1)
        print(f'O número {N1} arredondado para cima fica {num_arren}')
    else:
        print('\033[1;31mOpção invalida\033[m')
        continue
    break
