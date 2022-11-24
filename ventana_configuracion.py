from tkinter import *
import tkinter as tk
from tkinter import ttk
from extraccion_dof import *
from weber_dao import manipulacion_bd


class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        manipulacion2 = manipulacion_bd()
        urlist = manipulacion2.consulta2()
        self.opcion=tk.StringVar()
        links=(urlist)
        self.combobox1=ttk.Combobox(self.ventana1, 
                                  width=50, 
                                  textvariable=self.opcion, 
                                  values=links)
        self.combobox1.current(0)
        self.combobox1.grid(column=0, row=1)
        self.boton1=tk.Button(self.ventana1, text="Elegir", command=lambda:[self.boton1.destroy(),self.recuperar()])
        self.boton1.grid(column=0, row=2)    


        # Lista palabras
        wordlist = manipulacion2.consulta()
        self.opcion1=tk.StringVar()
        palabras=(wordlist)
        self.combobox2=ttk.Combobox(self.ventana1, 
                                  width=50, 
                                  textvariable=self.opcion1, 
                                  values=palabras)
        self.combobox2.current(0)
        self.combobox2.grid(column=0, row=4)
        self.boton2=tk.Button(self.ventana1, text="Elegir", command=lambda:[self.boton2.destroy(),self.recuperar1()])
        self.boton2.grid(column=0, row=5) 


        # Lista dominios
        lista_dominios = manipulacion2.consulta3()
        self.opcion2=tk.StringVar()
        dominios=(lista_dominios)
        self.combobox3=ttk.Combobox(self.ventana1, 
                                  width=50, 
                                  textvariable=self.opcion2, 
                                  values=dominios)
        self.combobox3.current(0)
        self.combobox3.grid(column=0, row=7)
        self.boton3=tk.Button(self.ventana1, text="Elegir", command=lambda:[self.boton3.destroy(),self.recuperar2()])
        self.boton3.grid(column=0, row=8)  
        self.ventana1.mainloop()


    def recuperar(self):
        seleccion = self.opcion.get()
        manipulacion = manipulacion_bd()
        btn_confirmar=Button(self.ventana1,text="Ok", command=lambda:[manipulacion.editar_url_usado(seleccion)])
        btn_confirmar.grid(row=1,column=2,padx=1, pady=6, ipady=4, ipadx=8)


    def recuperar1(self):
        seleccion1 = self.opcion1.get()
        manipulacion = manipulacion_bd()
        btn_confirmar2=Button(self.ventana1,text="Ok", command=lambda:[manipulacion.editar_palabra_usada(seleccion1)])
        btn_confirmar2.grid(row=1,column=10,padx=1, pady=6, ipady=4, ipadx=8)


    def recuperar2(self):
        seleccion2 = self.opcion2.get()
        manipulacion = manipulacion_bd()
        btn_confirmar3=Button(self.ventana1,text="Ok", command=lambda:[manipulacion.editar_dominio_usado(seleccion2)])
        btn_confirmar3.grid(row=1,column=17,padx=1, pady=6, ipady=4, ipadx=8)


aplicacion1=Aplicacion()