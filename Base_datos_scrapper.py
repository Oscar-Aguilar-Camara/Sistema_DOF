import mysql.connector
from tkinter import *
from prueba_gifs import aparecer_gifs

class conexion_bd():
    '''
    Clase que establece la conexión a la Base de datos 
    '''
    def __init__(self):
        
        self.conexion=mysql.connector.connect(
            host='localhost',
            port='3306' ,
            user='root' ,
            db='scraper2'
            )
            
        self.cursor = self.conexion.cursor()
        lbl = Label(text="Conectando a la base de datos")
        lbl.grid(row=1,column=1,padx=1, pady=4, ipadx=20,ipady=3)
        aparecer_gifs.aparecer_mensaje_1()

    def close_connection(self):
        '''
        Función que envia los datos a la Base de datos,
        y cierra la conexion a la bd
        '''
        self.conexion.commit()
        self.conexion.close()
        
        lbl2 = Label(text="Conexión a la base de datos cerrada")
        lbl2.grid(row=4,column=3,padx=1, pady=4, ipadx=20,ipady=3)

        lbl3 = Label(text="Proceso finalizado")
        lbl3.grid(row=5,column=3,padx=1, pady=4, ipadx=20,ipady=3)

        aparecer_gifs.aparecer_mensaje_7()
        
        #print("Proceso finalizado")


    