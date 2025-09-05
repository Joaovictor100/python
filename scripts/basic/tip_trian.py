'''Classificar tipo de triângulo'''
print('Classificar tipo de triângulo')
ERROR = False
try:
	L1 = float(input('Digite o primeiro lado: '))
	L2 = float(input('Digite o segundo lado: '))
	L3 = float(input('Digite o terceiro lado: '))
except ValueError:
	ERROR = True
# Verifica se ouve erro ou se os lados informados não formam um triângulo
if ERROR:
	print('Erro de digitação, tente novamente')
elif L1 < (L2+L3) and L2 < (L1+L3) and L3 < (L1+L2):
	if L1 == L2 and L2 == L3:
		TIP = 'Equilatero'
	elif L1 != L2 and L1 != L3 and L2 != L3:
		TIP = 'Escaleno'
	else:
		TIP = 'Isoseles'
	print(f'O tipo de triângulo digitado é: \033[35m{TIP}\033[m')
	print('Fim do Programa')
else:
	print('Os lados informados não formam um triangulo, tente novamente')
