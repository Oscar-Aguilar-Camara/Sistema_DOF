from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count

from extraccion_dof import extraccion

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

filemenu = Menu(menubar, tearoff=0)
# Crear comandos de los menus 
filemenu.add_command(label="Configuración")
filemenu.add_command(label="Monitoreo")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")
# Agregamos los menus a la barra de menus 
menubar.add_cascade(label="Opciones", menu=filemenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)


lbl1 = Label(root,text="nnn")

lbl1.grid(row=2,column=3,padx=1, pady=4, ipadx=20,ipady=3)
lbl = ImagenLabel(root)
lbl.grid(row=2,column=1,padx=1, pady=4, ipadx=2,ipady=3)

lbl.cargar_gif("loading.gif") # nombre o ruta de la imagen
root.mainloop()