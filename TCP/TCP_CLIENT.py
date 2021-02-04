'''
@adrlvma e @MayconArthuso

---------------------------------------------------------------
Criação do Cliente utilizando protocolo TCP para chat
---------------------------------------------------------------

Fontes:
    Documentação Socket
'''

#---------------------------------------------------------------
# Importar Bibliotecas
#---------------------------------------------------------------
import socket

ClientMultiSocket   = socket.socket()                           # Crie o socket

host                = '127.0.0.1'                               # Defina o endereço de hospedeiro - string com endereço IPV4.
port                = 2004                                      # Defina a porta do processo - inteiro.

print('Aguardando a resposta da conexão')                       # Informando a espera da conexão

try:
    ClientMultiSocket.connect((host, port))                     # Faça a conxão com um socket remoto - ("Endereço IPV4":Porta).
except socket.error as e:                                       # Cerque possíveis erros.
    print(str(e))                                               # Informe o erro ocorrido.

res = ClientMultiSocket.recv(1024)                              # A função recebe dados do socket.

while True:
    Input = input('Digite algo: ')                              # Capture a mensagem informada pelo usuário.
    ClientMultiSocket.send(str.encode(Input))                   # Envie dados para o socket cuja ligação foi estabelecida.

ClientMultiSocket.close()                                        # Uma vez finalizado o método multi_threaded_client encerre a conexão.
