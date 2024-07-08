import socket

# Informando o nome do HOST (URL)
strHost = input('\nInforme o nome do HOST ou URL do site: ')

# Obter uma tupla (hostname, aliaslist, ipaddrlist)
tupInfo = socket.gethostbyname_ex(strHost)
print(f'\n{tupInfo}\n')