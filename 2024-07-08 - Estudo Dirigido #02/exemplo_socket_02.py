import socket

# Informando o nome do HOST (URL)
strHost = input('\nInforme o nome do HOST ou URL do site: ')

# Obter o endereço IPV4 do HOST
strIPHost = socket.gethostbyname(strHost)
print(strIPHost)

# Obter uma tupla (hostname, aliaslist, ipaddrlist)
tupInfo = socket.gethostbyaddr(strIPHost)
print(f'\n{tupInfo}\n')