'''Reajuste Salarial'''
SA = int(input('Digite seu salario: '))
IR = int(input('Digite seu aumento em porcentagem: '))

# Formula da porcentagem
SR = SA/100*IR+SA

# Mostre
print(f'Seu salário era {SA} com o aumento de {IR}% fica {SR}')
