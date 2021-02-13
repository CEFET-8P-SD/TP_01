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

        self.pls = Label(self.login, text="Digite endereço IP", font=("Arial", 16), justify=CENTER)
        self.pls.place(relheight=0.1, relx=0.15, rely=0.1)

        self.labelIp = Label(self.login, text="IP: ")
        self.labelIp.place(relheight=0.1, relx=0.2, rely=0.2)

        self.entryIP = Entry(self.login)
        self.entryIP.place(relwidth=0.5, relheight=0.10, relx=0.30, rely=0.2)
        self.entryIP.focus()

        self.pls2 = Label(self.login, text="Digite seu nome", font=("Arial", 16), justify=CENTER)
        self.pls2.place(relheight=0.1, relx=0.15, rely=0.35)

        self.labelName = Label(self.login, text="Nome: ")
        self.labelName.place(relheight=0.1, relx=0.2, rely=0.45)

        self.entryName = Entry(self.login)
        self.entryName.place(relwidth=0.5, relheight=0.10, relx=0.30, rely=0.45)

        self.labelProtocolo = Label(self.login, text="Escolha um protocolo", font=("Arial", 16), justify=CENTER)
        self.labelProtocolo.place(relheight=0.2, relx=0.15, rely=0.55)

        self.select = StringVar()
        self.select.set("TCP")

        self.opt1 = Radiobutton(self.login, text="TCP", variable=self.select, value="TCP")
        self.opt1.place(relheight=0.12, relx=0.2, rely=0.7)

        self.opt2 = Radiobutton(self.login, text="UDP", variable=self.select, value="UDP")
        self.opt2.place(relheight=0.12, relx=0.35, rely=0.7)

        self.go = Button(self.login,
                         text="CONTINUE",
                         command=lambda: self.init_chat(self.entryIP.get(), self.entryName.get()))
        self.go.place(relx=0.4, rely=0.85)

        self.Window.mainloop()

    def init_chat(self, ip, name):
        if ip == "" or ip is None or name == "" or name is None:
            return

        self.login.destroy()
        if self.select.get() == "TCP":
            os.system("python3 TCP_tkinter/client.py " + ip + " " + name)
        else:
            os.system("python3 UDP_tkinter/client.py " + ip + " " + name)


if __name__ == '__main__':
    g = GUI()
