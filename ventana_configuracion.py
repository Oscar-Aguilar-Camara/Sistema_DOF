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
        diassemana=(urlist)
        self.combobox1=ttk.Combobox(self.ventana1, 
                                  width=50, 
                                  textvariable=self.opcion, 
                                  values=diassemana)
        self.combobox1.current(0)
        self.combobox1.grid(column=0, row=1)
        
        self.boton1=tk.Button(self.ventana1, text="Elegir", command=lambda:[self.boton1.destroy(),self.recuperar()])
        self.boton1.grid(column=0, row=2)    
        self.ventana1.mainloop()

    def recuperar(self):
        sele = self.opcion.get()
        manipulacion = manipulacion_bd()
        btn_confirmar=Button(self.ventana1,text="Ok", command=lambda:[manipulacion.editar_url_usado(sele)])
        btn_confirmar.grid(row=1,column=2,padx=1, pady=6, ipady=4, ipadx=8)

    
aplicacion1=Aplicacion()