from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time


# cliente se conectando ao chat
def cliente_conectando_chat():
    while True:
        connection, cliente = SERVER.accept()
        print(f'{cliente} se conectou ao chat')
        connection.send(bytes('Bem vindo ao chat com TCP!', 'utf8'))
        time.sleep(0.3)
        connection.send(bytes('Agora digite seu nome e pressione enter!', 'utf8'))
        addresses[connection] = cliente
        Thread(target=comunicacao_mensagem, args=(connection,)).start()


# Handles a single client connection
def comunicacao_mensagem(client):
    name = client.recv(BUFSIZ).decode('utf8')
    client.send(bytes(f'Bem vindo {name}!', 'utf8'))
    time.sleep(0.3)
    client.send(bytes('Se você quer sair, escreva \'{quit}\' para sair.', 'utf8'))
    enviar_mensagem(bytes(f'{name} se juntou ao chat!', 'utf8'))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes('{quit}', 'utf8'):
            enviar_mensagem(msg, name + ': ')
        else:
            client.send(bytes('{quit}', 'utf8'))
            client.close()
            del clients[client]
            enviar_mensagem(bytes(f'{name} saiu do chat.', 'utf8'))
            break


# Enviando uma mensagem para todos os clients ativos no chat
def enviar_mensagem(msg, prefix=''):
    for sock in clients:
        sock.send(bytes(prefix, 'utf8') + msg)


clients = {}
addresses = {}

HOST = ''
PORT = 33001
BUFSIZ = 1024
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind((HOST, PORT))

if __name__ == "__main__":
    SERVER.listen(2)
    print('Esperando para conexão...')
    ACCEPT_THREAD = Thread(target=cliente_conectando_chat)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
