import pygame
from tkinter import *

pygame.init()

janela = Tk()

def rojao():
    pygame.mixer.music.load("rojao.mp3")
    pygame.mixer.music.play()

def taca():
    pygame.mixer.music.load("taca.mp3")
    pygame.mixer.music.play()

def cafe():
    pygame.mixer.music.load("cafe.mpeg")
    pygame.mixer.music.play()

def cu():
    pygame.mixer.music.load("cu.mpeg")
    pygame.mixer.music.play()
    
bt_rojao = Button(janela, text="Rojão", command=rojao)
bt_rojao["font"] = ("Arial", "25")
bt_rojao.config(bg="darkblue", foreground="white")
bt_rojao.place(x=40, y=30)

bt_taca = Button(janela, text="Taca o pau", command=taca)
bt_taca["font"] = ("Arial", "25")
bt_taca.config(bg="darkgreen", foreground="white")
bt_taca.place(x=180, y=30)

bt_cafe = Button(janela, text="Café", command=cafe)
bt_cafe["font"] = ("Arial", "25")
bt_cafe.config(bg="brown", foreground="white")
bt_cafe.place(x=410, y=30)

bt_cu = Button(janela, text="Ai meu c#", command=cu)
bt_cu["font"] = ("Arial", "25")
bt_cu.config(bg="black", foreground="white")
bt_cu.place(x=40, y=120)

janela.geometry("600x400")
janela.resizable(width=False, height=False)
janela.title("Sons diversos")
janela.mainloop()
