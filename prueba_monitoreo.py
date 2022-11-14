from tkinter import *
import tkinter as tk
from Base_datos_scrapper import conexion_bd

from extraccion_dof import extraccion

'''

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
        label = ImagenLabel(root)
        label.grid(row=1,column=2,padx=1, pady=4, ipadx=2,ipady=3)
        label.cargar_gif("loading.gif") # nombre o ruta de la imagen


    def aparecer_mensaje_2():
        #desaparecemos el gif anterior
    
        #creamos imagen finalizado para la anterior funcion
        #imagen = PhotoImage(file="correcto.png")
        #Label(root, image=imagen, bd=0)
        #Label.grid(row=2,column=2,padx=1, pady=4, ipadx=2,ipady=3)
    
        # cargamos gif loading
        label2 = ImagenLabel(root)
        label2.grid(row=2,column=2,padx=1, pady=4, ipadx=2,ipady=3)
        label2.cargar_gif("loading.gif") # nombre o ruta de la imagen


    def aparecer_mensaje_3():
        # cargamos gif loading
        lbl3 = ImagenLabel(root)
        lbl3.grid(row=3,column=2,padx=1, pady=4, ipadx=2,ipady=3)
        lbl3.cargar_gif("loading.gif") # nombre o ruta de la imagen
        # cargamos gif loading
        lbl4 = ImagenLabel(root)
        lbl4.grid(row=4,column=2,padx=1, pady=4, ipadx=2,ipady=3)
        lbl4.cargar_gif("loading.gif") # nombre o ruta de la imagen


    def aparecer_mensaje_4():
        # cargamos gif loading
        lbl5 = ImagenLabel(root)
        lbl5.grid(row=5,column=2,padx=1, pady=4, ipadx=2,ipady=3)
        lbl5.cargar_gif("loading.gif") # nombre o ruta de la imagen


    def aparecer_mensaje_5():
        # cargamos gif loading
        lbl6 = ImagenLabel(root)
        lbl6.grid(row=6,column=2,padx=1, pady=4, ipadx=2,ipady=3)
        lbl6.cargar_gif("loading.gif") # nombre o ruta de la imagen
        # cargamos gif loading
        lbl7 = ImagenLabel(root)
        lbl7.grid(row=7,column=2,padx=1, pady=4, ipadx=2,ipady=3)
        lbl7.cargar_gif("loading.gif") # nombre o ruta de la imagen


    def aparecer_mensaje_6():
        # cargamos gif loading
        lbl8 = ImagenLabel(root)
        lbl8.grid(row=8,column=2,padx=1, pady=4, ipadx=2,ipady=3)
        lbl8.cargar_gif("loading.gif") # nombre o ruta de la imagen


    def aparecer_mensaje_7():
        # cargamos gif loading
        lbl9 = ImagenLabel(root)
        lbl9.grid(row=9,column=2,padx=1, pady=4, ipadx=2,ipady=3)
        lbl9.cargar_gif("loading.gif") # nombre o ruta de la imagen
        # cargamos gif loading
        lbl10 = ImagenLabel(root)
        lbl10.grid(row=10,column=2,padx=1, pady=4, ipadx=2,ipady=3)
        lbl10.cargar_gif("loading.gif") # nombre o ruta de la imagen
'''

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

#  Obtenemos el largo y  ancho de la pantalla
wtotal = root.winfo_screenwidth()
htotal = root.winfo_screenheight()

#  Guardamos el largo y alto de la ventana
wventana = 700
hventana = 500

#  Aplicamos la siguiente formula para calcular donde debería posicionarse
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)

#  Se lo aplicamos a la geometría de la ventana
root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
# Finalmente bucle de la aplicación
extraccion = extraccion()
conexion_bd = conexion_bd()
# creamos boton de ejecutar 
btn_ejecutar = Button(root, text="Ejecutar Servicio", command=lambda:[extraccion.acceso_web() , extraccion.buscar_69b(),extraccion.obtener_link(), extraccion.validar_pub_nva(), extraccion.notificacion_correo()])
#btn_ejecutar = Button(root, text="Ejecutar Servicio", command=lambda:[aparecer_mensaje_1(),extraccion.acceso_web() , aparecer_mensaje_2(), extraccion.buscar_69b(),aparecer_mensaje_3() ,extraccion.obtener_link(), aparecer_mensaje_4(),extraccion.validar_pub_nva(), extraccion.notificacion_correo(), aparecer_mensaje_5(), aparecer_mensaje_6(), aparecer_mensaje_7()])
btn_ejecutar.place(x=300, y=200)

root.mainloop()