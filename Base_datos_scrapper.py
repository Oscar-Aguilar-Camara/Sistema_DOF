import mysql.connector

def connection():
    try:
        global connection
        connection=mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            db='scraper'
        )

        if connection.is_connected():
            print('Conexión exitosa')

    except Exception as ex:
        print(ex)
    global cursor 
    #Comprobación de conexión a la base de datos
    cursor = connection.cursor()
    cursor.execute('SELECT DATABASE()')
    row = cursor.fetchone()
    print('Conectado a la base de datos: {}'.format(row))

def close_connection():
    #Cerrar la conexión
    connection.close()
    print('Conexión cerrada exitosamente')
