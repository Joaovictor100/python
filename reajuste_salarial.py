'''Reajuste Salarial'''
print('\033[1;34mReajuste Salarial\033[m\n')
ERRO = '\033[1;31mOpção invalida\033[m'
REEN = '\033[1;31mOpção invalida Reentre\033[m '

# Contadores e Acumuladores
CT = 0
CG = 0
CDF = 0
CGF = 0
MP = 0

# Loop, Laço
while True:
    NF = input('Digite o nome do funcionario: ').strip().title()
    SA = float(input('Digite o seu salario: '))
    
    # FILTRO DE ERRO
    F = ''
    LP = 0
    while F not in ('1', '2', '3'):
        # Este while é repetido enquanto o usuario digitar '1' ou '2' ou '3'
        
        if LP == 1:
            print(ERRO)
        LP = 1
        F = input('''Escolha a opção
        [ 1 ] Técnico
        [ 2 ] Gerente
        [ 3 ] Demais funcionarios
        ''').strip()
    if F == '1':
        FF = 'Técnico' # Cargo (Função)
        IR = 50 # Indice de Reajuste
        CT = CT+1 # Contador do Funcionario 'Técnico'
    elif F == '2':
        FF = 'Gerente'
        IR = 30
        CG = CG+1
    elif F == '3':
        FF = 'Demais funcionarios'
        IR = 10
        CDF = CDF+1
        
    SR = SA+(SA*IR)/100 # Reajuste
    CGF = CGF+1 # Contador do Total de Funcionarios com o salario reajustado
    MP = MP+SR # Montante do salario de todos os funcionarios
    
    print('Exibindo Relatorio...')
    print(f'''Funcionario: {NF}
Salario atual: {SA}
Função: {FF}
Indice de reajuste: {IR}%
Salario reajustado: {SR}
''')

    # Verifica se o usuario quer repetir o processo com outro funcionario
    # Se não há outro funcionario, exibe o relatorio final.
    OP = input('Há outro funcionario? (S/N) ').strip().title()
    while OP not in ('S', 'N'):
        OP = input(REEN).strip().title()
    if OP == 'S':
        continue
    if OP == 'N':
        print('Exibindo relatorio final')
        print(f'''Total de:
    Técnico: {CT}
    Gerente: {CG}
    Demais Funcionarios: {CDF}
    Geral: {CGF}
    Montante: {MP}''')
        print('Fim do processo')
        break
