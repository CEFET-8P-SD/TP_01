from socket import socket, AF_INET, SOCK_DGRAM
from datetime import datetime

class Server:

    def __init__(self):
        self.__num = 0

        self.__servidor_sk = socket(AF_INET, SOCK_DGRAM)

        host    = ''
        porta   = 5000

        destino = (host, porta)

        self.__servidor_sk.bind(destino)

        self.__clientes    = []
        self.__destinos = {}

    '''
    def _run(self):
        
        print("Inicializando servidor")

        while True:

            dado_1, cliente = self.__servidor_sk.recvfrom(2048)

            dado = dado_1.decode()

            if cliente in self.__clientes:
                aux = self.__tratando_dado(dado)

                if aux[1]== '{quit}':
                    self.__encerrando_conexao(aux[0])
                    break
                else:
                    self.__enviando_msm_chat(aux[1], aux[0])

            else:
                
                self.__primeira_conexão(nome=dado, destino=cliente)
                mensagem = "Cliente {} entrou no chat;".format(dado)
                self.__enviando_msm_chat(mensagem, self.__num)
    '''

    def _run(self):

        print("*** Servidor de comunicação UDP iniciando. ***. \n\n")
        print("Protocolo de inicialização bem sucedido. \n\n")

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

        mensagem_3 = "                    *** Seu nome é {} ***                    ".format(nome)

        self.__clientes.append(cliente)
        self.__destinos[cliente] = nome

        print(destino)

        return nome

servidor = Server()
servidor._run()