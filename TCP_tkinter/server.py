from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
from datetime import datetime


class Server:
    def __init__(self):
        self.__clients = {}
        self.__addresses = {}
        self.__HOST = ''
        self.__PORT = 33001
        self.__BUFSIZ = 1024
        self.__SERVER = socket(AF_INET, SOCK_STREAM)
        self.__SERVER.bind((self.__HOST, self.__PORT))

    def run(self):
        self.__SERVER.listen(2)
        print('Esperando para conexão...')
        client_thread = Thread(target=self.__cliente_conectando_chat)
        client_thread.start()
        client_thread.join()
        self.__SERVER.close()

    # cliente se conectando ao chat
    def __cliente_conectando_chat(self):
        while True:
            connection, client = self.__SERVER.accept()
            print(f'{client} se conectou ao chat')
            connection.send(bytes('Bem vindo ao chat com TCP!', 'utf8'))
            self.__addresses[connection] = client
            Thread(target=self.__comunicacao_mensagem, args=(connection, client)).start()

    # comunicacao do cliente no chat
    def __comunicacao_mensagem(self, conn_client, client):
        name = conn_client.recv(self.__BUFSIZ).decode('utf8')
        conn_client.send(bytes(f'Bem vindo {name}!', 'utf8'))
        time.sleep(0.3)
        conn_client.send(bytes('Se você quer sair, escreva \'{quit}\' para sair.', 'utf8'))
        self.__enviar_mensagem(bytes(f'{name} se juntou ao chat!', 'utf8'))
        self.__clients[conn_client] = name

        while True:
            msg = conn_client.recv(self.__BUFSIZ)
            if msg != bytes('{quit}', 'utf8'):
                self.__enviar_mensagem(msg, datetime.now().strftime('%H:%M:%S') + ' ' + name + ': ')
            else:
                conn_client.send(bytes('{quit}', 'utf8'))
                print(f'{client} se desconectou do chat')
                conn_client.close()
                del self.__clients[conn_client]
                self.__enviar_mensagem(bytes(f'{name} saiu do chat.', 'utf8'))
                break

    # Enviando uma mensagem para todos os clients ativos no chat
    def __enviar_mensagem(self, msg, prefix=''):
        for sock in self.__clients:
            sock.send(bytes(prefix, 'utf8') + msg)


server = Server()
server.run()
