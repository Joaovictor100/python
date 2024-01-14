'''Converter Bases numericas'''
var = input('Digite um número ou palavra: ')
alt = int(input('''Escolha a opção que deseja converter
\t[ 1 ] String em BINÁRIO
\t[ 2 ] Número em BINÁRIO
\t[ 3 ] Número em OCTAL
\t[ 4 ] Número em HEXADECIMAL\n\n'''))

#FILTRO DE ERRO
if alt == 1:
    DTA_T = ' '.join(format(ord(array_p), 'b') for array_p in var)
    TIPO = 'BINÁRIO'
    DTA = 'string'
elif alt == 2:
    var = int(var)
    DTA_T = str(bin(var))[2:]
    TIPO = 'BINÁRIO'
    DTA = 'número'
elif alt == 3:
    var = int(var)
    DTA_T = str(oct(var))[2:]
    TIPO = 'OCTAL'
    DTA = 'número'
elif alt == 4:
    var = int(var)
    DTA_T = str(hex(var))[2:]
    TIPO = 'HEXADECIMAL'
    DTA = 'número'
else:
    print('Opção inválida, Tente novamante')

print(f'O (A) \033[1;34m{DTA}\033[m | {var} | em {TIPO} fica:\n\n\t\t\033[1;31m{DTA_T}\033[m')
