'''Cor de font Trabalhando com \033[m'''
print('\t\t\tEditar cor de font\n')

LOOP_INFINITO = True

while LOOP_INFINITO:
    style = input('''Digite a opção para o estilo da font:\n
    0. nulo\n
    1. \033[1mEstilo em negrito\033[m\n
    2. \033[3mEltilo negativo\033[m\n
    3. \033[4mEstilo sublinhado\033[m\n\n\t''').strip()
    
    if style not in ('1', '2', '3', '0'):
        print('\033[31mOpção invalida\033[m')
        break
    
    style = style.replace('3', '4')
    style = style.replace('2', '3')
    
    background = input('''Digite a opção para o fundo da font:\n
    0. nulo\n
    1. \033[41mVermelho\033[m\n
    2. \033[42mVerde\033[m\n
    3. \033[43mAmarelo\033[m\n
    4. \033[44mAzul\033[m\n
    5. \033[45mRosa\033[m\n
    6. \033[46mAzul-esverdeado\033[m\n\n\t''').strip()
    
    if background not in ('1', '2', '3', '4', '5', '6', '0'):
        print('\033[31mOpção invalida\033[m')
        break
    
    background = '4'+background
    # Concatenção de '4'+background.
    # '4' para o \033[m significa mexendo com o fundo da letra.
    # E a variavel 'background' é o numero da opção de cor do fundo.
    # No caso se digitar 2, vai ficar 42, que seria um background verde.
    
    color = input('''Digite a opção para o cor da font:\n
    1. \033[31mVermelho\033[m\n
    2. \033[32mVerde\033[m\n
    3. \033[33mAmarelo\033[m\n
    4. \033[34mAzul\033[m\n
    5. \033[35mRosa\033[m\n
    6. \033[36mAzul-esverdeado\033[m\n
    7. nulo\n\n\t''').strip()
    
    if color not in ('1', '2', '3', '4', '5', '6', '7'):
        print('\033[31mOpção invalida\033[m')
        break
    
    color = '3'+color
    
    palavra = input('Digite uma palavra: ')
    print(f'\n\t\t\033[{style};{color};{background}m{palavra}\033[m')
    
    op = input('Deseja fazer isso de novo? (S/N) or (Y/N) default N ').strip().upper()
    if op in ('S', 'Y'):
        print(10*'\n')
        continue
    if op == 'N':
        break
    break
