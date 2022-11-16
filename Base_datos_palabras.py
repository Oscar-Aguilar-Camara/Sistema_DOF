import mysql.connector
# from extraccion_dof import extraccion
   
conexion=mysql.connector.connect(
host='localhost',
port='3306' ,
user='root' ,
db='scraper2'
)
            
def consulta(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * from lista_palabras;")
    wordlist = cursor.fetchall()
    cursor.close()
    conexion.close()

    return wordlist
