from matplotlib.pyplot import *

plot([1, 2, 3, 4], [10, 15, 25, 30])
title('Meu primeiro gráfico')

plot([1, 2, 3, 4], [10, 15, 25, 30], 'r--')
show()

subplot(2, 1, 1)  # 2 linhas, 1 coluna, primeiro gráfico
plot([1, 2, 3, 4], [10, 15, 25, 30])

subplot(2, 1, 2)  # 2 linhas, 1 coluna, segundo gráfico
bar(['A', 'B', 'C', 'D'], [3, 7, 1, 10])

show()

savefig('meu_grafico.png')
