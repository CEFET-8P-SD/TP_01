# import socket programming library
import socket
# import thread module
from _thread import *


# thread function
def multi_threaded_client(connection, cliente):
    connection.send(str.encode('Server is working:'))
    while True:
        # dados vindo do cliente
        data = connection.recv(2048)
        print(f'msg cliente {cliente[1]}: {data.decode()}')
        if not data:
            print('Adeus')
            break

    print(f'Finalizando conexao do cliente {cliente}')
    connection.close()


# cria o server socket
ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 2004
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

# coloca o socket no modo ouvindo ativo
ServerSocket.listen(5)
print(f'Socket está ouvindo na porta {port}')

while True:
    # estabelecer conexão com o cliente
    connection, cliente = ServerSocket.accept()
    print(f'Conectado no endereço {cliente[0]} : {str(cliente[1])}')
    # dispara uma nova thread e retorna um id de identificacao
    start_new_thread(multi_threaded_client, (connection, cliente))

ServerSideSocket.close()
