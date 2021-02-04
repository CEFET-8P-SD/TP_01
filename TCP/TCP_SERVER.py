'''
@adrlvma e @MayconArthuso

---------------------------------------------------------------
Criação do Servidor utilizando protocolo TCP para chat
---------------------------------------------------------------

Fontes:
    Documentação Socket
'''

#---------------------------------------------------------------
# Importar Bibliotecas
#---------------------------------------------------------------
from _thread import start_new_thread
import socket

#---------------------------------------------------------------
# Criação do Método de recepção das mensgens
#---------------------------------------------------------------
def multi_threaded_client(connection, cliente):
    connection.send(str.encode('Server is working:'))                                   # Uma vez gerada a comunicação, envie uma mensagem identificando isso.
    while True:
        data    = connection.recv(2048)                                                 # A função recebe dados do socket - Do cliente.
        print(f'msg cliente {cliente[1]}: {data.decode()}')                             # Imprima a mensagem recebida do Cliente.

        if not data:                                                                    # Caso a mensagem seja None.
            print('Adeus')                                                              # Imprima a mensgem de termino.
            break                                                                       # Saía do While e encerre o método.

    print(f'Finalizando conexao do cliente {cliente}')                                  # Imprima a mensagem de termino de conxão.
    connection.close()                                                                  # Feche a conexão estabelecida anteriormente.


#---------------------------------------------------------------
# Criando Socket e configurando conexão
#---------------------------------------------------------------
ServerSocket    = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)         # Crie um socket da família AF_INET do tipo SOCK_STREAM.

host            = '127.0.0.1'                                                           # Defina o endereço de hospedeiro - string com endereço IPV4.
port            = 2004                                                                  # Defina a porta do processo - inteiro.
ThreadCount     = 0              

try:
    ServerSocket.bind((host, port))                                                     # Faça a ligação do socket com o address - ("Endereço IPV4":Porta).
except socket.error as e:                                                               # Cerque possíveis erros.
    print(str(e))                                                                       # Informe o erro ocorrido.


ServerSocket.listen(5)                                                                  # Ative o modo "Ouvindo": "Habilite o software aceitar conexões".
print(f'Socket está ouvindo na porta {port}.')                                          # Informe que o Socket está ativo e informe a porta.

#---------------------------------------------------------------
# Estabelecer conexão
#---------------------------------------------------------------
while True:
   
    connection, cliente = ServerSocket.accept()                                         # Estabelecer conexão com o cliente retornando (conn, address).  
    print(f'Conectado no endereço {cliente[0]} : {str(cliente[1])}')                    # Informe a conexão com o Cliente ("Endereço IPV4":Porta).
    start_new_thread(multi_threaded_client, (connection, cliente))                      # Dispare uma nova Thread que cuidará de "multi_threaded_client" e retorne um id.

ServerSideSocket.close()                                                                # Uma vez finalizado o método multi_threaded_client encerre a conexão.
