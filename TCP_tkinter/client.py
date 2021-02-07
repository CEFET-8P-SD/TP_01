from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter


# receber mensagens.
def receber_mensagem():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode('utf8')
            msg_list.insert(tkinter.END, msg)
        except OSError:
            break


# enviar mensagens
def enviar_mensagem(event=None):
    msg = my_msg.get()
    my_msg.set('')  # limpar campo de escrita.
    client_socket.send(bytes(msg, 'utf8'))
    if msg == '{quit}':
        client_socket.close()
        top.quit()


# fechar a janela de chat
def fechar_chat(event=None):
    my_msg.set('{quit}')
    enviar_mensagem()


top = tkinter.Tk()
top.title('Chat usando Protocolo TCP')
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

HOST = '127.0.0.1'
PORT = 33001
BUFSIZ = 1024

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((HOST, PORT))

receive_thread = Thread(target=receber_mensagem)
receive_thread.start()
tkinter.mainloop()
