import sys, os, socket

# Arquivo de Entrada
dirInput = os.path.dirname(os.path.abspath(__file__))
strNomeArq = f'{dirInput}\\portas.txt' 

# Ler arquivo e montar uma lista
lstPorts = list()
try:
    with open(strNomeArq, 'r') as arqInput:
        for strLinha in arqInput:
            lstPorts.append(strLinha[:-1].split(';'))
except:
    sys.exit(f'\nERRO: {sys.exc_info()[0]}\n')
else:
    # Solicitar URL do HOST e obter o seu respectivo IP
    strURL = input('\nInforme a URL do HOST: ')
    ipHost = socket.gethostbyname(strURL)

    # Iterar a lista de portas
    for portTest in lstPorts:
        protType = socket.SOCK_STREAM if portTest[1] == 'TCP' else socket.SOCK_DGRAM 
        sockTest = socket.socket(family=socket.AF_INET, type=protType)
        try:
            conn = sockTest.connect((ipHost, int(portTest[0])))
        except:
            print(f'Porta {portTest[0]:>5}/{portTest[1]}:{portTest[2]} ... ERRO: {sys.exc_info()[0]}')
        else:
            print(f'Porta {portTest[0]:>5}/{portTest[1]}:{portTest[2]} ... OK!!!!!')
            sockTest.close()