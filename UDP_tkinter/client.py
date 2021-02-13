from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
import tkinter
import sys

cliente = socket(AF_INET, SOCK_DGRAM)

# ---------------------------------------------------------
#   Definindo o endereço de destino - conjunto (ip, porta)
# ---------------------------------------------------------
host = '127.0.0.1'
user_name = sys.argv[2]
port = 33000
BUFSIZ = 1024
destino = (host, port)


def primeira_conexao():
    input_msg = ""
    cliente.sendto(input_msg.encode(), destino)


def nome_usuario():
    cliente.sendto(user_name.encode(), destino)


# ---------------------------------------------------------
#   Configurando métodos de envia e chegada
# ---------------------------------------------------------
def receber_mensagem():
    while True:
        try:
            msg = cliente.recv(BUFSIZ).decode('utf8')
            msg_list.insert(tkinter.END, msg)
        except OSError:
            break


def enviar_mensagem(event=None):
    input_msg = my_msg.get()
    my_msg.set('')
    cliente.sendto(input_msg.encode(), destino)

    if input_msg == '{quit}':
        cliente.close()
        top.quit()


def fechar_chat(event=None):
    my_msg.set('{quit}')
    enviar_mensagem()


primeira_conexao()
nome_usuario()

# ---------------------------------------------------------
#   Configurando Interface de comunicação com o cliente
# ---------------------------------------------------------
top = tkinter.Tk()
top.title('Protocolo UDP')
top.resizable(width=True, height=True)

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()
my_msg.set('')

scrollbar = tkinter.Scrollbar(messages_frame)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

msg_list = tkinter.Listbox(messages_frame, height=25, width=70, yscrollcommand=scrollbar.set)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg, width=65)
entry_field.bind('<Return>', enviar_mensagem)
entry_field.pack()
entry_field.focus()

send_button = tkinter.Button(top, text='Enviar', font='Helvetica 10 bold', width=20, command=enviar_mensagem)
send_button.pack()

top.protocol('WM_DELETE_WINDOW', fechar_chat)

receive_thread = Thread(target=receber_mensagem)
receive_thread.start()
tkinter.mainloop()
