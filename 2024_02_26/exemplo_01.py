import sys
from funcoes import * 

# Informando os valores de entrada
tamLista = 50
minValor = -15
maxValor = 15

# Gerando a lista
lstValores = gerarLista_v1(tamLista, minValor, maxValor)

if not lstValores[0]:
    print(lstValores[1])
    sys.exit()

print(lstValores[1])