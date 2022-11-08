import mysql.connector

class conexion_bd():
    '''
    Clase que establece la conexión a la Base de datos 
    '''
    def __init__(self):
        
        self.conexion=mysql.connector.connect(
            host='localhost',
            port='3306' ,
            user='root' ,
            db='scraper'
            )
            
        self.cursor = self.conexion.cursor()


    def close_connection(self):
        '''
        Función que envia los datos a la Base de datos,
        y cierra la conexion a la bd
        '''
        self.conexion.commit()
        self.conexion.close()
        
        print('Conexión a la base de datos cerrada exitosamente')
        print("Proceso finalizado")


    