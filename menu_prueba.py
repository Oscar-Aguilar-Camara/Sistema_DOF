from tkinter import *
import tkinter as tk
from tkinter import ttk
from extraccion_dof import *
from weber_dao import manipulacion_bd
# from funcion_agregar_palabra import agregar


ventana = tk.Tk()
ventana.title("Configuración")
ventana.geometry("800x400")

# Evento clic botón cambiar dirección web
def cambio_direccion():
    liga= StringVar()
    manipulacion = manipulacion_bd()   
    nva_link=Entry(ventana,bg="white",textvariable=liga)
    nva_link.grid(row=1,column=1,padx=1, pady=4, ipadx=20,ipady=3) 
    btn_guardar=Button(ventana,text="Guardar",command=lambda:[nva_link.destroy(),btn_guardar.destroy(),manipulacion.insertar_cambio_direccion(liga.get())])
    btn_guardar.grid(row=1,column=2,padx=1, pady=6, ipady=4, ipadx=8)


# Evento clic botón cambiar dominio web
def cambiar_dominio_web():
    manipulacion = manipulacion_bd()
    cuadro_texto2=Entry(ventana,bg="white")
    cuadro_texto2.grid(row=2,column=1,padx=1, pady=4, ipadx=20,ipady=3)
    cambio_dominio=cuadro_texto2.get()
    r=str(cambio_dominio)
    btn_guardar2=Button(ventana,text="Guardar", command=lambda:[manipulacion.consulta_link_nuevo()])
    btn_guardar2.grid(row=2,column=2,padx=1, pady=6, ipady=4, ipadx=8)
    

# Evento botón aparecer lista de palabras
def aparecer_lista():
    combo=ttk.Combobox(ventana, values=wordlist)
    for index, word in enumerate (wordlist):
        combo.insert(index,word[0])
    combo.grid(row=0,column=1,padx=1, pady=6)
    combo.current(0)
    btn_agregar=Button(ventana,text="Agregar", command=agregar_palabra)
    btn_agregar.grid(row=0,column=2,padx=1, pady=6, ipady=4, ipadx=8)

def aparecer_lista2():
    opcion=tk.StringVar()
    links = urlist
    combo = ttk.Combobox(ventana, 
                                  width=10, 
                                  textvariable=opcion, 
                                  values=links)
    combo.grid(row=1,column=3,padx=1, pady=6)

    combo.current(0)

    selec = combo.bind("<<ComboboxSelected>>" ,opcion.get())
    print(selec)
    btn_agregar=Button(ventana,text="Usar", command=recuperar)
    btn_agregar.grid(row=1,column=4,padx=1, pady=6, ipady=4, ipadx=8)
   

def recuperar(self):
    sele = self.opcion.get()
    print(sele)


def agregar_palabra():
    palabra= StringVar()
    manipulacion = manipulacion_bd()
    nva_palabra = Entry(ventana, bg="white", textvariable=palabra)
    nva_palabra.grid(row=0,column=3,padx=1, pady=6, ipady=4, ipadx=8)
    btn_confirmar=Button(ventana,text="Ok", command=lambda:[manipulacion.insertar_palabra_nueva(palabra.get()), aparecer_lista()])
    btn_confirmar.grid(row=0,column=4,padx=1, pady=6, ipady=4, ipadx=8)


# Establecimiento de la conexión a la base de datos
manipulacion = manipulacion_bd()
wordlist = manipulacion.consulta()

manipulacion2 = manipulacion_bd()
urlist = manipulacion2.consulta2()


# Botones de configuración
btn_consultar_palabras = Button(ventana,text="Ver palabras en lista", command=lambda:[aparecer_lista(),aparecer_lista2()])
btn_consultar_palabras.grid(row=0,column=0,padx=20, pady=20, sticky="w",ipady=6)

btn_cambiar_direccion = Button(ventana,text="Cambiar dirección web ", command=cambio_direccion)
btn_cambiar_direccion.grid(row=1,column=0,padx=20, pady=20, sticky="w",ipady=6)

btn_cambiar_dominio = Button(ventana,text="Cambiar dominio web ", command=cambiar_dominio_web)
btn_cambiar_dominio.grid(row=2,column=0,padx=20, pady=20, sticky="w",ipady=6)

ventana.mainloop()