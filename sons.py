import pygame
from tkinter import *

class Tela:

    def __init__(self, master):
        pygame.init()

        cab = PhotoImage(file="cab.png")
        self.img = Label(janela, image=cab)
        self.img.cab = cab
        self.img.place(x=0, y=530)
        
        self.bt_rojao = Button(janela, text="ROJÃO")
        self.bt_rojao["font"] = ("Arial", "25")
        self.bt_rojao.config(bg="#87CEEB", foreground="black")
        self.bt_rojao.place(x=40, y=30)
        self.bt_rojao.bind("<Button-1>", self.rojao)

        self.bt_taca = Button(janela, text="TACA O PAU")
        self.bt_taca["font"] = ("Arial", "25")
        self.bt_taca.config(bg="#87CEEB", foreground="BLACK")
        self.bt_taca.place(x=200, y=30)
        self.bt_taca.bind("<Button-1>", self.taca)

        self.bt_cafe = Button(janela, text="CAFÉ")
        self.bt_cafe["font"] = ("Arial", "25")
        self.bt_cafe.config(bg="#87CEEB", foreground="BLACK")
        self.bt_cafe.place(x=445, y=30)
        self.bt_cafe.bind("<Button-1>", self.cafe)

        self.bt_cu = Button(janela, text="AI MEU C#")
        self.bt_cu["font"] = ("Arial", "25")
        self.bt_cu.config(bg="#87CEEB", foreground="BLACK")
        self.bt_cu.place(x=580, y=30)
        self.bt_cu.bind("<Button-1>", self.cu)

        self.fechar = Button(janela, text="X")
        self.fechar["font"] = ("Arial", "25")
        self.fechar.config(bg="brown", foreground="white")
        self.fechar.place(x=710, y=450)
        self.fechar.bind("<Button-1>", self.fecharr)

    

    def fecharr(self, event):
        janela.destroy()
        exit()

    def rojao(self, event):
        pygame.mixer.music.load("rojao.mp3")
        pygame.mixer.music.play()

    def taca(self, event):
        pygame.mixer.music.load("taca.mp3")
        pygame.mixer.music.play()

    def cafe(self, event):
        pygame.mixer.music.load("cafe.mpeg")
        pygame.mixer.music.play()

    def cu(self, event):
        pygame.mixer.music.load("cu.mpeg")
        pygame.mixer.music.play()

janela = Tk()
Tela(janela)

janela.geometry("810x600")
janela.resizable(width=False, height=False)
janela.title("Sons diversos")
janela.mainloop()
