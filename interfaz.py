from Base_datos_scrapper import conexion_bd
from extraccion_dof import extraccion
# from extractor import *
from tkinter import *
import tkinter as tk


# Configuración de la raíz
root = tk.Tk()
root.title("Weber")
root.iconbitmap("img/scrapy.ico")
root.geometry('700x500')
root.resizable(width=0, height=0)
# Se crea la barra de menú
menubar = Menu(root)
root.config(menu=menubar)
# cremos los menus 
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

# destruir boton despues de cliquear
def destruir_boton():
    btn_ejecutar.destroy()


# creamos boton de ejecutar 
btn_ejecutar = Button(root, text="Ejecutar Servicio", command=lambda:[destruir_boton(),extraccion.acceso_web() , extraccion.buscar_69b(), extraccion.obtener_link(), extraccion.validar_pub_nva(), extraccion.notificacion_correo()])
btn_ejecutar.place(x=300, y=200)
root.mainloop()