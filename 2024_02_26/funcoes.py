import random
from constantes import *


def gerarLista_v1(tamanhoLista: int, menorValor: int, maiorValor: int):
    # Verificando se os argumentos são de tipos válidos
    if not isinstance(tamanhoLista, int): 
        return False, f'O argumento {COR_AMARELA}tamanhoLista{COR_BRANCA} deve ser do tipo {COR_AZUL}inteiro{COR_BRANCA}...'
    if not isinstance(menorValor, int): 
        return False, f'O argumento {COR_AMARELA}menorValor{COR_BRANCA} deve ser do tipo {COR_AZUL}inteiro{COR_BRANCA}...'
    if not isinstance(maiorValor, int): 
        return False, f'O argumento {COR_AMARELA}maiorValor{COR_BRANCA} deve ser do tipo {COR_AZUL}inteiro{COR_BRANCA}...'

    # Verificando se menorValor < maiorValor
    if menorValor > maiorValor:
        return False, f'O argumento menorValor deve ser menor que o argumento maiorValor...'
    
    # Gerando a lista de retorno
    lstRetorno = [random.randint(menorValor, maiorValor) for _ in range(tamanhoLista)]
    return True, lstRetorno
    

def gerarLista_v2(tamanhoLista: int, menorValor: int, maiorValor: int):
    boolSucesso = False
    strMensagem = None
    lstRetorno  = None
    
    # Verificando se os argumentos são de tipos válidos
    if not isinstance(tamanhoLista, int): 
        strMensagem = 'O argumento tamanhoLista deve ser do tipo inteiro...'
    elif not isinstance(menorValor, int): 
        strMensagem = 'O argumento menorValor deve ser do tipo inteiro...'
    elif not isinstance(maiorValor, int): 
        strMensagem = 'O argumento maiorValor deve ser do tipo inteiro...'
    elif menorValor > maiorValor:
        strMensagem = 'O argumento menorValor deve ser menor que o argumento maiorValor...'
    else:
        # Gerando a lista de retorno
        lstRetorno = [random.randint(menorValor, maiorValor) for _ in range(tamanhoLista)]
        boolSucesso = True
    
    return boolSucesso, lstRetorno, strMensagem
