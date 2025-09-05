import sympy as sp

x = sp.symbols('x')
pesos = sp.symbols('pesos')

def minha_funcao(x, pesos):
    return x*pesos

y = minha_funcao(x, pesos)
derivada_simbolica = sp.diff(y, x)

print(derivada_simbolica)
