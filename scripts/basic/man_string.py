'''Manipulação de string'''

nome = input('Digite o seu nome: ').strip()
# strip() tira espaços na frente e traz da string

print('Analisando seu nome ...')
print(f'Seu nome {nome.title()}')
# title() deixa 'joao victor' em 'Joao Victor'

print(f'Seu nome em maiúsculo {nome.upper()}')
# upper() deixa 'JOAO VICTOR' em 'joao victor'

print(f'Seu nome em minúsculo {nome.lower()}')
# lower() deixa 'joao victor' em 'JOAO VICTOR'

print(f'Seu nome tem {len(nome)-nome.count(" ")} letras')
# len conta o numero de caracteres
# count conta quantidade de itens pesquisados
# no caso acima tira os aspaços para somente contar letras

nome = nome.split()
nome = nome[0]
# conseguir primeiro nome, dividindo em listas entre os espaços

print(f'Seu primeiro nome têm {len(nome)} letras')
