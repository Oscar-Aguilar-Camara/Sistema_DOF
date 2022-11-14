from Base_datos_scrapper import conexion_bd

class Configurar_palabras:
        def __init__(self):
                self.cont_palabras = 0
                self.conexion = conexion_bd()     
                self.conexion.cursor.execute("SELECT * FROM `lista_palabras` WHERE palabra = %s;", (self.cont_palabras[self.cont_palabras],))
                self.valores = self.fetchall()
                self.conexion = conexion_bd()  
                self.conexion.cursor.execute("INSERT INTO `lista_palabras` (`id`, `palabra`) VALUES (NULL, 'Yucatán')") 
                for filas in self.conexion:
                        print (filas)

