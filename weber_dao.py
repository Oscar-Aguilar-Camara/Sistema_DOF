from Base_datos_scrapper import conexion_bd
from extraccion_dof import *
from tkinter import *


class manipulacion_bd():
    
    def __init__(self):
        self.palabra=""
        
    
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


    def consulta(conexion):
        conexion = conexion_bd() 
        conexion.cursor.execute("SELECT `palabra` from lista_palabras;")
        wordlist = conexion.cursor.fetchall()
        conexion.cursor.close()
        conexion.close_connection()
        return wordlist


    def insertar_palabra_nueva(self, palabra):
        self.palabra = palabra
        conexion = conexion_bd()
        conexion.cursor.execute("INSERT INTO `lista_palabras` (`id`, `palabra`) VALUES (NULL,%(word)s)",{"word":self.palabra}) 
        print (self.palabra)
        conexion.close_connection()
    

    def consulta2(conexion):
        conexion = conexion_bd() 
        conexion.cursor.execute("SELECT `link` from cambio_link;")
        wordlist = conexion.cursor.fetchall()
        conexion.cursor.close()
        conexion.close_connection()
        return wordlist


    def insertar_cambio_direccion(self, direccion):
        self.direccion = direccion
        conexion = conexion_bd()
        conexion.cursor.execute("INSERT INTO `cambio_link` (`id`, `link`) VALUES (NULL,%(liga)s)",{"liga":self.direccion}) 
        print (self.direccion)
        conexion.close_connection()


    
    def consulta_link_nuevo(self):
        conexion = conexion_bd()
        conexion.cursor.execute("SELECT `link` FROM `cambio_link` WHERE id = 1;")
        self.valores = conexion.cursor.fetchall()
        print(self.valores)
    
    '''
    def url_usado(self):
        conexion = conexion_bd()
        conexion.cursor.execute("SELECT `url` from url_en_uso WHERE id = 1;")
        self.liga = conexion.cursor.fetchall()
        #print(self.liga)
    '''

    def editar_url_usado(self, url_nuevo):
        self.url_nuevo = url_nuevo
        conexion = conexion_bd()
        conexion.cursor.execute("UPDATE `url_en_uso` SET `url` = %(liga)s WHERE `url_en_uso`.`id` = 1;",{"liga":self.url_nuevo})
        print (self.url_nuevo)
        conexion.close_connection()


    def url_usado():
        conexion = conexion_bd()
        conexion.cursor.execute("SELECT `url` from url_en_uso WHERE id = 1; ")
        url = conexion.cursor.fetchall()
        res = [str(x) for x in url]
        chars = "('),"
        nvo_url = ''.join( x for x in res if x not in chars)
    
        nvo_url = ''.join( x for x in nvo_url if x not in chars)
        conexion.close_connection()
    
        return nvo_url