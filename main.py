import socket
from tkinter import *


class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()

        self.login = Toplevel()
        self.login.title("Login")
        self.login.resizable(width=False, height=False)
        self.login.configure(width=400, height=300)

        self.pls = Label(self.login, text="Please login to continue", justify=CENTER)
        self.pls.place(relheight=0.15, relx=0.2, rely=0.07)

        self.labelName = Label(self.login, text="Name: ")
        self.labelName.place(relheight=0.2, relx=0.1, rely=0.2)

        self.entryName = Entry(self.login)
        self.entryName.place(relwidth=0.4, relheight=0.12, relx=0.35, rely=0.2)
        self.entryName.focus()

        self.labelProtocolo = Label(self.login, text="Escolha um protocolo", justify=CENTER)
        self.labelProtocolo.place(relheight=0.2, relx=0.2, rely=0.35)

        self.select = IntVar()
        self.select.set(1)

        self.opt1 = Radiobutton(self.login, text="TCP", variable=self.select, value=1)
        self.opt1.place(relheight=0.2, relx=0.2, rely=0.5)

        self.opt2 = Radiobutton(self.login, text="UDP", variable=self.select, value=2)
        self.opt2.place(relheight=0.2, relx=0.35, rely=0.5)

        self.go = Button(self.login,
                         text="CONTINUE",
                         command=lambda: self.goAhead(self.entryName.get()))
        self.go.place(relx=0.4, rely=0.70)

        self.Window.mainloop()

    def goAhead(self, name):
        self.login.destroy()


if __name__ == '__main__':
    PORT = 5000
    SERVER = "127.0.1.1"
    ADDRESS = (SERVER, PORT)
    FORMAT = "utf-8"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDRESS)
    g = GUI()
