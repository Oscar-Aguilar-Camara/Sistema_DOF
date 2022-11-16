from Base_datos_scrapper import conexion_bd
from extraccion_dof import *
from tkinter import *


class manipulacion_bd():
    def consulta_links(self, lst_nva_pub, cont_link_dominio, lst_link_dominio):
        '''
        Función que hace la consulta de los links existentes en la Base de datos
        '''
        conexion = conexion_bd()  
        conexion.cursor.execute("SELECT * FROM `extraccion` WHERE link = %s;", (lst_link_dominio[cont_link_dominio],))
        self.valores = conexion.cursor.fetchall()
            # Si no encuentra coincidencia del link en la base de datos se considera nueva y se almacena en una nueva lista
        if bool(self.valores) == False:
            lst_nva_pub.append(lst_link_dominio[cont_link_dominio])
            # print(lst_nva_pub)
    
        conexion.close_connection() 
        return lst_nva_pub
        

    def insertar_links(self, lst_nva_pub, today, cont_liga):
        '''
        Función que inserta los link nuevos a la Base de datos
        '''
        conexion = conexion_bd()  
        conexion.cursor.execute("INSERT INTO `extraccion` (`id`, `link`, `fecha`) VALUES (NULL,%(liga)s, %(fecha_actual)s)",{"liga":lst_nva_pub[cont_liga],"fecha_actual":today}) 
        # print("links que se insertan...")
        # print(lst_nva_pub[cont_liga])
        conexion.close_connection()


    def insertar_palabra_nueva():
        conexion = conexion_bd()
        conexion.cursor.execute("INSERT INTO `lista_palabras` (`id`, `palabra`) VALUES (NULL,%(word)s)",{"word":"México"}) 
        conexion.close_connection()

  