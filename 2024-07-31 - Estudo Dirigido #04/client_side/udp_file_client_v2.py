import socket

SERVER = '127.0.0.1'
PORT   = 31435

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF, 25000)

while True:
    strNomeArq = input('Nome do arquivo a fazer download: ')
    sock.sendto(strNomeArq.encode('utf-8'), (SERVER, PORT))

    fd = open (strNomeArq, 'wb')

    tam = 0
    data, addr = sock.recvfrom(4096)
    while data != b'':
        tam += len(data)
        print (f'Recebi {len(data) / tam} bytes')
        fd.write (data)
        data, addr = sock.recvfrom(4096)

    fd.close()

sock.close()