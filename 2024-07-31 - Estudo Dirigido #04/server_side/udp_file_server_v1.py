import socket

INTERFACE = '127.0.0.1'
PORT      = 31435

sock = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((INTERFACE, PORT))

print ('Escutando em ...', (INTERFACE, PORT))

while True:
    # Recebe o nome do arquivo a servir
    data, source = sock.recvfrom(512)

    # Abre o arquivo a servir ao cliente
    strFileName = data.decode('utf-8')
    print ('Recebi pedido para o arquivo ', strFileName)
    fd = open (strFileName, 'rb')

    # Lê o conteúdo do arquivo a enviar ao cliente
    print ('Enviando arquivo ...', strFileName)
    fileData = fd.read(4096)
    sock.sendto(fileData, source)

    # Fecha o arquivo
    fd.close()

sock.close()