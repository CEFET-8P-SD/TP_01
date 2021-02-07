from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
from datetime import datetime


# cliente se conectando ao chat
def cliente_conectando_chat():
    while True:
        connection, client = SERVER.accept()
        print(f'{client} se conectou ao chat')
        connection.send(bytes('Bem vindo ao chat com TCP!', 'utf8'))
        time.sleep(0.3)
        connection.send(bytes('Agora digite seu nome e pressione enter!', 'utf8'))
        addresses[connection] = client
        Thread(target=comunicacao_mensagem, args=(connection, client)).start()


# comunicacao do cliente no chat
def comunicacao_mensagem(conn_client, client):
    name = conn_client.recv(BUFSIZ).decode('utf8')
    conn_client.send(bytes(f'Bem vindo {name}!', 'utf8'))
    time.sleep(0.3)
    conn_client.send(bytes('Se você quer sair, escreva \'{quit}\' para sair.', 'utf8'))
    enviar_mensagem(bytes(f'{name} se juntou ao chat!', 'utf8'))
    clients[conn_client] = name

    while True:
        msg = conn_client.recv(BUFSIZ)
        if msg != bytes('{quit}', 'utf8'):
            enviar_mensagem(msg, datetime.now().strftime('%H:%M:%S') + ' ' + name + ': ')
        else:
            conn_client.send(bytes('{quit}', 'utf8'))
            print(f'{client} se desconectou do chat')
            conn_client.close()
            del clients[conn_client]
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
