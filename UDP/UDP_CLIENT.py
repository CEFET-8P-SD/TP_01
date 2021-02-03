import socket

HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
print('Para sair use CTRL+X')
msg = input('msg: ')

while msg != '\x18':
    udp.sendto(msg.encode(), dest)
    msg = input('msg: ')
udp.close()
