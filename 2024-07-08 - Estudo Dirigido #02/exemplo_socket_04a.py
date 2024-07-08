import socket

# Informando o nome do HOST (URL) e a porta de comunicação
strHost = input('\nInforme o nome do HOST ou URL do site: ')
intPort = 80

# Exibindo informações do HOST
# (family, type, proto, canonname, sockaddr)
tupInfo = socket.getaddrinfo(strHost, intPort)
print(f'\n{tupInfo}\n')

for info in tupInfo:
   print('----------------------------------------')
   print(f'Info ...................: {info}')
   print(f'Family .................: {info[0]}')
   print(f'Type ...................: {info[1]}')
   print(f'Proto ..................: {info[2]}')
   print(f'Canonical Name (CNAME) .: {info[3]}')   
   print(f'SOCKET Address .........: {info[4]}')

print('----------------------------------------\n')