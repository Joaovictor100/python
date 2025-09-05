'''Coversor de moedas'''
print('Conversão de moedas')

vc = input('''Escolha a opção
            1. converter para Reais
            2. converter para Dolares
            3. converter para Euros
                    ''')
ta = input('''Escolha a moeda atual
            1. Reais
            2. Dolares
            3. Euros
                    ''')
QD = float(input('Digite a quantidade de moeda: '))

# Filtro de erro
if ta == '1' and vc == '2':
	C = QD/4.91
	VAL = 'reais'
	CON = 'dolares'
	
elif ta == '2' and vc == '1':
    C = QD*4.91
    VAL = 'dolares'
    CON = 'reais'
    
elif ta == '3' and vc == '1':
	C = QD*5.42
	VAL = 'euros'
	CON = 'reais'
	
elif ta == '1' and vc == '3':
	C = QD/5.42
	VAL = 'reais'
	CON = 'eutos'
	
elif ta == '3' and vc == '2':
	C = QD*1.1
	VAL = 'euros'
	CON = 'dolares'
	
elif ta == '2' and vc == '3':
	C = QD/1.1
	VAL = 'dolares'
	CON = 'euros'

else:
    print('Opção invalida')
    
print(f'De {VAL} para {CON} fica {C:.2f}')
