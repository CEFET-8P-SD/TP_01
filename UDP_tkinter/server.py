from socket import socket, AF_INET, SOCK_DGRAM
from datetime import datetime


class Server:
    def __init__(self):
        self.__num = 0
        self.__servidor_sk = socket(AF_INET, SOCK_DGRAM)
        self.__clientes = []
        self.__destinos = {}

        host = ''
        porta = 5000
        self.__servidor_sk.bind((host, porta))

    def _run(self):
        print("*** Servidor de comunicação UDP iniciando. ***.")
        print("Protocolo de inicialização bem sucedido. \n")

        while True:
            codigo, cliente = self.__servidor_sk.recvfrom(2048)
            mensagem = codigo.decode()

            if cliente in self.__clientes:
                if mensagem == '{quit}':
                    self.__encerrando_conexao(cliente)
                else:
                    nome = self.__destinos[cliente]
                    mensagem = "{}: {}".format(nome, mensagem)
                    self.__enviando_msm_chat(mensagem)

            else:
                nome = self.__primeira_conexao(cliente)
                mensagem = "{} conectou-se ao chat".format(nome)

                self.__enviando_msm_chat(mensagem)

    def __enviando_msm_chat(self, mensagem):
        hora = datetime.now().strftime('%H:%M:%S')

        for cliente in self.__clientes:
            mensagem_2 = "{} {}".format(hora, mensagem)
            self.__servidor_sk.sendto(mensagem_2.encode(), cliente)

    def __encerrando_conexao(self, cliente):
        nome = self.__destinos[cliente]
        mensagem = "{} Saiu do chat.".format(nome)

        self.__enviando_msm_chat(mensagem)
        self.__destinos.pop(cliente)

    def __primeira_conexao(self, destino):
        mensagem_1 = "Bem vindo ao protocolo de comunicação UDP."
        self.__servidor_sk.sendto(mensagem_1.encode(), destino)

        mensagem_2 = "Agora que está conectado, informe seu nome:"
        self.__servidor_sk.sendto(mensagem_2.encode(), destino)

        nome_c, cliente = self.__servidor_sk.recvfrom(2048)
        nome = nome_c.decode()

        self.__clientes.append(cliente)
        self.__destinos[cliente] = nome
        print(destino)

        return nome


servidor = Server()
servidor._run()
