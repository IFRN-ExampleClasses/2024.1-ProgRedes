import socket

#------------------------------------------------------------
def get_protnumber(prefix):
   return dict ((getattr(socket, a), a)
      for a in dir(socket)
         if a.startswith(prefix) )
#------------------------------------------------------------

proto_fam = get_protnumber('AF_')
types     = get_protnumber('SOCK_')
protocols = get_protnumber('IPPROTO_')

# Informando o nome do HOST (URL) e a porta de comunicação
strHost = input('\nInforme o nome do HOST ou URL do site: ')
intPort = 80

# Exibindo informações do HOST
# (family, type, proto, canonname, sockaddr)
# socket.getaddrinfo(host, port, family=0, type=0, proto=0, flags=0)
tupInfo = socket.getaddrinfo(host=strHost, port=intPort)
print(f'\n{tupInfo}\n')

for info in tupInfo:
   family, socktype, proto, canonname, sockaddr = info
   print('----------------------------------------')
   print(f'Info ...................: {info}')
   print(f'Family .................: {proto_fam[family]}')
   print(f'Type ...................: {types[socktype]}')
   print(f'Proto ..................: {protocols[proto]}')
   print(f'Canonical Name (CNAME) .: {canonname}')   
   print(f'SOCKET Address .........: {sockaddr}')

print('----------------------------------------\n')