import socket

HOST = ''  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)

while True:
    data, cliente = udp.recvfrom(1024)
    print(f'msg cliente {cliente[1]}: {data.decode()}')
udp.close()
