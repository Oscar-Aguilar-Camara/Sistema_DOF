import mysql.connector
# from extraccion_dof import extraccion

class conexion_bd():
    
    def __init__(self):
        
        self.conexion=mysql.connector.connect(
            host='localhost',
            port='3306' ,
            user='root' ,
            db='scraper'
            )
            
        self.cursor = self.conexion.cursor()


    def close_connection(self):
        #Cerrar la conexión
        #Envío de los valores a la base de datos
        self.conexion.commit()
        self.conexion.close()
        print('Conexión a la base de datos cerrada exitosamente')
        print("Proceso finalizado")


    