from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count

class ImagenLabel(tk.Label):
    """creamos una label para meter el gif"""
    def cargar_gif(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.tiempo = im.info['duracion']
        except:
            self.tiempo = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def bajar_gif(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.tiempo, self.next_frame)

root = tk.Tk()
root.title("Weber")
root.iconbitmap("img/scrapy.ico")
root.geometry('700x500')
root.resizable(width=0, height=0)
# Se crea la barra de menú
menubar = Menu(root)
root.config(menu=menubar)
lbl = ImagenLabel(root)
lbl.pack()
lbl.cargar_gif("wow.gif") # nombre o ruta de la imagen
root.mainloop()