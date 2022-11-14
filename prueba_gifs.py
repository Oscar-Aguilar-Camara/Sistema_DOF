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


class aparecer_gifs():
    def aparecer_mensaje_1():
        # cargamos gif loading
        label = ImagenLabel()
        label.grid(row=1,column=2,padx=1, pady=4, ipadx=2,ipady=3)
        label.cargar_gif("loading.gif") # nombre o ruta de la imagen
        
        #Destruimos el label
        label.after(1000, label.destroy())
        
        #creamos imagen finalizado para la anterior funcion
        label_correcto = ImagenLabel()
        label_correcto.grid(row=1,column=2,padx=1, pady=4, ipadx=2,ipady=3)
        label_correcto.cargar_gif("correcto.png") # nombre o ruta de la imagen

    def aparecer_mensaje_2():
        # cargamos gif loading
        label2 = ImagenLabel()
        label2.grid(row=2,column=2,padx=1, pady=4, ipadx=2,ipady=3)
        label2.cargar_gif("loading.gif") # nombre o ruta de la imagen

        #Destruimos el label
        label2.after(1000, label2.destroy())
        
        #creamos imagen finalizado para la anterior funcion
        label_correcto = ImagenLabel()
        label_correcto.grid(row=2,column=2,padx=1, pady=4, ipadx=2,ipady=3)
        label_correcto.cargar_gif("correcto.png") # nombre o ruta de la imagen


    def aparecer_mensaje_3():
        # cargamos gif loading
        label3 = ImagenLabel()
        label3.grid(row=3,column=2,padx=1, pady=4, ipadx=2,ipady=3)
        label3.cargar_gif("loading.gif") # nombre o ruta de la imagen
        #Destruimos el label
        label3.after(1000, label3.destroy())
        #creamos imagen finalizado para la anterior funcion
        label_correcto = ImagenLabel()
        label_correcto.grid(row=3,column=2,padx=1, pady=4, ipadx=2,ipady=3)
        label_correcto.cargar_gif("correcto.png") # nombre o ruta de la imagen

        # cargamos gif loading
        label4 = ImagenLabel()
        label4.grid(row=4,column=2,padx=1, pady=4, ipadx=2,ipady=3)
        label4.cargar_gif("loading.gif") # nombre o ruta de la imagen
        #Destruimos el label
        label4.after(1000, label4.destroy())
        #creamos imagen finalizado para la anterior funcion
        label_correcto = ImagenLabel()
        label_correcto.grid(row=4,column=2,padx=1, pady=4, ipadx=2,ipady=3)
        label_correcto.cargar_gif("correcto.png") # nombre o ruta de la imagen


    def aparecer_mensaje_4():
        # cargamos gif loading
        label5 = ImagenLabel()
        label5.grid(row=5,column=2,padx=1, pady=4, ipadx=2,ipady=3)
        label5.cargar_gif("loading.gif") # nombre o ruta de la imagen
        #Destruimos el label
        label5.after(1000, label5.destroy())
        #creamos imagen finalizado para la anterior funcion
        label_correcto = ImagenLabel()
        label_correcto.grid(row=5,column=2,padx=1, pady=4, ipadx=2,ipady=3)
        label_correcto.cargar_gif("correcto.png") # nombre o ruta de la imagen


    def aparecer_mensaje_5():
        # cargamos gif loading
        label6 = ImagenLabel()
        label6.grid(row=1,column=4,padx=1, pady=4, ipadx=2,ipady=3)
        label6.cargar_gif("loading.gif") # nombre o ruta de la imagen
        #Destruimos el label
        label6.after(1000, label6.destroy())
        #creamos imagen finalizado para la anterior funcion
        label_correcto = ImagenLabel()
        label_correcto.grid(row=1,column=4,padx=1, pady=4, ipadx=2,ipady=3)
        label_correcto.cargar_gif("correcto.png") # nombre o ruta de la imagen
        
        # cargamos gif loading
        label7 = ImagenLabel()
        label7.grid(row=2,column=4,padx=1, pady=4, ipadx=2,ipady=3)
        label7.cargar_gif("loading.gif") # nombre o ruta de la imagen
        #Destruimos el label
        label7.after(1000, label7.destroy())
        #creamos imagen finalizado para la anterior funcion
        label_correcto = ImagenLabel()
        label_correcto.grid(row=2,column=4,padx=1, pady=4, ipadx=2,ipady=3)
        label_correcto.cargar_gif("correcto.png") # nombre o ruta de la imagen


    def aparecer_mensaje_6():
        # cargamos gif loading
        label8 = ImagenLabel()
        label8.grid(row=3,column=4,padx=1, pady=4, ipadx=2,ipady=3)
        label8.cargar_gif("loading.gif") # nombre o ruta de la imagen
        #Destruimos el label
        label8.after(1000, label8.destroy())
        #creamos imagen finalizado para la anterior funcion
        label_correcto = ImagenLabel()
        label_correcto.grid(row=3,column=4,padx=1, pady=4, ipadx=2,ipady=3)
        label_correcto.cargar_gif("correcto.png") # nombre o ruta de la imagen


    def aparecer_mensaje_7():
        # cargamos gif loading
        label9 = ImagenLabel()
        label9.grid(row=4,column=4,padx=1, pady=4, ipadx=2,ipady=3)
        label9.cargar_gif("loading.gif") # nombre o ruta de la imagen
        #Destruimos el label
        label9.after(1000, label9.destroy())
        #creamos imagen finalizado para la anterior funcion
        label_correcto = ImagenLabel()
        label_correcto.grid(row=4,column=4,padx=1, pady=4, ipadx=2,ipady=3)
        label_correcto.cargar_gif("correcto.png") # nombre o ruta de la imagen

        # cargamos gif loading
        label10 = ImagenLabel()
        label10.grid(row=5,column=4,padx=1, pady=4, ipadx=2,ipady=3)
        label10.cargar_gif("loading.gif") # nombre o ruta de la imagen
        #Destruimos el label
        label10.after(1000, label10.destroy())
        #creamos imagen finalizado para la anterior funcion
        label_correcto = ImagenLabel()
        label_correcto.grid(row=5,column=4,padx=1, pady=4, ipadx=2,ipady=3)
        label_correcto.cargar_gif("correcto.png") # nombre o ruta de la imagen

