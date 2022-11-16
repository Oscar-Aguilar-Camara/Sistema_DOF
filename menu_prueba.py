from tkinter import *
from Base_datos_palabras import *
import tkinter as tk
from tkinter import ttk
from extraccion_dof import *
from weber_dao import manipulacion_bd
# from funcion_agregar_palabra import agregar


ventana = tk.Tk()
ventana.title("Configuración")
ventana.geometry("600x300")

# Evento clic botón cambiar dirección web
def cambiar_direccion_web():
    cuadro_texto1=Entry(ventana,bg="white")
    cuadro_texto1.grid(row=1,column=1,padx=1, pady=4, ipadx=20,ipady=3)
    cambio_direccion=cuadro_texto1.get()
    r=str(cambio_direccion)
    btn_guardar=Button(ventana,text="Guardar")
    btn_guardar.grid(row=1,column=2,padx=1, pady=6, ipady=4, ipadx=8)


# Evento clic botón cambiar dominio web
def cambiar_dominio_web():
    cuadro_texto2=Entry(ventana,bg="white")
    cuadro_texto2.grid(row=2,column=1,padx=1, pady=4, ipadx=20,ipady=3)
    cambio_dominio=cuadro_texto2.get()
    r=str(cambio_dominio)
    btn_guardar2=Button(ventana,text="Guardar")
    btn_guardar2.grid(row=2,column=2,padx=1, pady=6, ipady=4, ipadx=8)
    

# Evento botón aparecer lista de palabras
def aparecer_lista():
    combo=ttk.Combobox(ventana, values=wordlist)
    for index, word in enumerate (wordlist):
        combo.insert(index,word[1])
    combo.grid(row=0,column=1,padx=1, pady=6)
    btn_agregar=Button(ventana,text="Agregar", command=agregar_palabra)
    btn_agregar.grid(row=0,column=2,padx=1, pady=6, ipady=4, ipadx=8)


def agregar_palabra():
    # agregar.creacion_label()
    # insertar = 
    palabra= StringVar()
    manipulacion = manipulacion_bd()
    nva_palabra = Entry(ventana, bg="white", textvariable=palabra)
    nva_palabra.grid(row=0,column=3,padx=1, pady=6, ipady=4, ipadx=8)
    btn_confirmar=Button(ventana,text="Ok", command=lambda:[manipulacion.insertar_palabra_nueva(palabra.get()), aparecer_lista()])
    btn_confirmar.grid(row=0,column=4,padx=1, pady=6, ipady=4, ipadx=8)
    



# Establecimiento de la conexión a la base de datos
wordlist = consulta(conexion)

# Botones de configuración
btn_consultar_palabras = Button(ventana,text="Ver palabras en lista", command=aparecer_lista)
btn_consultar_palabras.grid(row=0,column=0,padx=20, pady=20, sticky="w",ipady=6)

btn_cambiar_direccion = Button(ventana,text="Cambiar dirección web ", command=cambiar_direccion_web)
btn_cambiar_direccion.grid(row=1,column=0,padx=20, pady=20, sticky="w",ipady=6)

btn_cambiar_dominio = Button(ventana,text="Cambiar dominio web ", command=cambiar_dominio_web)
btn_cambiar_dominio.grid(row=2,column=0,padx=20, pady=20, sticky="w",ipady=6)



ventana.mainloop()