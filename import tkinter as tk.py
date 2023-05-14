import tkinter as Re  
import datetime

class TelaPrincipal:
    def __init__(self, master):
        self.nossaTela = master
        self.lblrelogio = Re.Label(
            self.nossaTela, font=('Calibri', 26),fg= 'black')
        self.lblrelogio.pack(pady=50, padx=50)
        self.alteracao() 

    def alteracao(self):
        now = datetime.datetime.now()
        self.lblrelogio['text'] = now.strftime('%H:%M:%S')
        self.nossaTela.after(1000, self.alteracao)

janelaRaiz = Re.Tk ()
TelaPrincipal(janelaRaiz)
janelaRaiz.mainloop()