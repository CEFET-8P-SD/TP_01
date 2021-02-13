from tkinter import *
import os


class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()

        self.login = Toplevel()
        self.login.title("Login")
        self.login.resizable(width=False, height=False)
        self.login.configure(width=400, height=300)

        self.pls = Label(self.login, text="Digite endereço IP", justify=CENTER)
        self.pls.place(relheight=0.15, relx=0.2, rely=0.07)

        self.labelName = Label(self.login, text="IP: ")
        self.labelName.place(relheight=0.2, relx=0.1, rely=0.2)

        self.entryName = Entry(self.login)
        self.entryName.place(relwidth=0.4, relheight=0.12, relx=0.35, rely=0.2)
        self.entryName.focus()

        self.labelProtocolo = Label(self.login, text="Escolha um protocolo", justify=CENTER)
        self.labelProtocolo.place(relheight=0.2, relx=0.2, rely=0.35)

        self.select = StringVar()
        self.select.set("TCP")

        self.opt1 = Radiobutton(self.login, text="TCP", variable=self.select, value="TCP")
        self.opt1.place(relheight=0.2, relx=0.2, rely=0.5)

        self.opt2 = Radiobutton(self.login, text="UDP", variable=self.select, value="UDP")
        self.opt2.place(relheight=0.2, relx=0.35, rely=0.5)

        self.go = Button(self.login,
                         text="CONTINUE",
                         command=lambda: self.init_chat())
        self.go.place(relx=0.4, rely=0.70)

        self.Window.mainloop()

    def init_chat(self):
        self.login.destroy()
        if self.select.get() == "TCP":
            os.system("python3 TCP_tkinter/client.py")
        else:
            os.system("python3 UDP_tkinter/client.py")


if __name__ == '__main__':
    g = GUI()
