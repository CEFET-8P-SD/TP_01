import socket

ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2004

print('Aguardando a resposta da conexão')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))

res = ClientMultiSocket.recv(1024)
while True:
    Input = input('Digite algo: ')
    ClientMultiSocket.send(str.encode(Input))

ClientMultiSocket.close()
