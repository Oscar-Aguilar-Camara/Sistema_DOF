from Base_datos_scrapper import *
import urllib.request
# para busqueda soup expresion regular 
from msilib.schema import Property
from bs4 import BeautifulSoup
import re 
#importamos para envios de correos 
import smtplib 
from email.message import EmailMessage 

#Establecer conexion con la página
def acceso_web():
    #Leer y decodificar la página
    global datos 
    datos = urllib.request.urlopen('https://www.dof.gob.mx/#gsc.tab=0').read().decode()


#Transformamos todo el HTML en un objeto de Beautiful Soap
def buscar_69b():
    global palabra 
    global resultado 
    global conteo
    soup = BeautifulSoup(datos)
    #Búsqueda de todas las etiquetas tr
    box = soup.find('tr',id="trcontent")
    #Búsqueda de las etiquetas a
    resultado = box.find_all('a',class_='enlaces')
    #Búsqueda de la palabra clave
    palabra = re.findall(r'69-B', str(resultado))
    print(palabra)
    #Contar elementos
    transforma = ", ".join(map(str, palabra))
    conteo = len(transforma.split())
    #print("Hay " + str(conteo) + " palabras encontradas.")

def obtener_link():
    #Recupera todos los link de las publicaciones y las almacena en una lista -links[]
    lst_links =[]
    for ref in resultado:
        tag=ref.get('href')+'\n'
        transforma="".join(map(str, tag))
        link=[transforma.split('\n')]
        lst_links.append(link)
        

    #Resguarda especialmente los links en donde se encuentre la palabra 69-B en una lista -lst_69B[]
    lst_69B =[]
    x=0
    for Pos_info in resultado:
        
        encuentra = re.findall(r'69-B', str(Pos_info))
        if bool(encuentra)==True:
            #print(encuentra)
            #print(resultado[x])
            #print(links[x])
            PosLink = lst_links[x]
            lst_69B.append(PosLink)
        
        x+=1
    # print (lst_69B)

    #Elimina carcateres innecesarios de los links y las concatena con el dominio de la pagina 
    global lst_link_dominio
    lst_link_dominio =[]
    for Textlink in lst_69B:
        cadena = Textlink[0]
        characters = "[]'"

        cadena = ''.join( x for x in cadena if x not in characters)
        cal='https://www.dof.gob.mx'+cadena
        lst_link_dominio.append(cal)
        print(cal)

def validar_pub_nva():
    #Obtener fecha actual
    from datetime import datetime

    today = datetime.now()
    print(today)

    # Validar si la publiacion es nueva o ya ha sido almacenada en la base de datos
    cont_link_dominio = 0
    global lst_nva_pub
    lst_nva_pub=[]
    for ciclo in range(conteo):
        cursor.execute("SELECT * FROM `extraccion` WHERE link = %s;", (lst_link_dominio[cont_link_dominio],))
        valores = cursor.fetchall()
        # print(lst_link_dominio[cont_link_dominio])
        # Si no encuentra coincidencia del link en la base de datos se considera nueva y se almacena en una nueva lista
        if bool(valores) == False:
            lst_nva_pub.append(lst_link_dominio[cont_link_dominio])

        cont_link_dominio+=1
    # print (cont_link_dominio)

    #Insercion de valores en la base de datos
    cont_lig = 0
    for ciclo in lst_nva_pub:
        cursor.execute("INSERT INTO `extraccion` (`id`, `link`, `fecha`) VALUES (NULL,%(liga)s, %(fecha_actual)s)",{"liga":lst_nva_pub[cont_lig],"fecha_actual":today})
        cont_lig+=1

    # Convertimos la lista de los links nuevos en cadena de texto
    global str_pubs_nva
    str_pubs_nva = ", ".join(lst_nva_pub)
    print(str_pubs_nva)

def notificacion_correo():
    if bool(lst_nva_pub) == True:
        asunto_correo = "Publicaciones del Diario Oficial de la Federación" 
        #correo_receptor = "frester_dui98@hotmail.com" 
        correo_remitente = "jnahuat@nasa.com.mx" 
        correo_receptor = "frester_dui98@hotmail.com"
        email_smtp = "smtp.office365.com" 
        contrasena_correo = "stckrhhmhjxfqwgl" #contraseña aplicacion Nasa
        #email_password = "poykyzptkdiihjhe" #contraseña aplicacion hotmail frester
    

        
        mensaje = EmailMessage() 

        # Configuracion de los titulos 
        mensaje['Subject'] = asunto_correo 
        mensaje['From'] = correo_remitente 
        mensaje['To'] = correo_receptor

        # Mensaje de texto que se enviará
        mensaje.set_content("Se ha identificado una nueva publicación referente al artículo 69-B: \n"+str_pubs_nva) 

        try:
            # smtp servidor y puerto 
            server = smtplib.SMTP('smtp.office365.com', port=587) 

            # Identificar este cliente en el servidor 
            server.ehlo() 

            # iniciar conexion del servidor SMTP
            server.starttls() 

            # Iniciar sesion con el correo electronico
            server.login(correo_remitente, contrasena_correo) 

            # se envia el mensaje por correo 
            server.send_message(mensaje) 

            # se cierra la conexion del servidor 
            server.quit()

            print('Correo electronico enviado con exito')
            
        except smtplib.SMTPException as e:
            print ('Error al intentar enviar el correo electronico, cuasa del error: ', e)

    if bool(lst_nva_pub) == False:
        asunto_correo = "Publicaciones del Diario Oficial de la Federación" 
        #correo_receptor = "frester_dui98@hotmail.com" 
        correo_remitente = "jnahuat@nasa.com.mx" 
        correo_receptor = "frester_dui98@hotmail.com"
        email_smtp = "smtp.office365.com" 
        contrasena_correo = "stckrhhmhjxfqwgl" #contraseña aplicacion Nasa
        #email_password = "poykyzptkdiihjhe" #contraseña aplicacion hotmail frester
    

        
        mensaje = EmailMessage() 

        # Configuracion de los titulos
        mensaje['Subject'] = asunto_correo 
        mensaje['From'] = correo_remitente 
        mensaje['To'] = correo_receptor

        # Mensaje que se le envia al correo
        mensaje.set_content("No se ha encontrado publicación nueva referente al articulo 69-B") 

        try:
            # smtp servidor y puerto 
            server = smtplib.SMTP('smtp.office365.com', port=587) 

            # Identificar este cliente en el servidor 
            server.ehlo() 

            # iniciar conexion del servidor SMTP
            server.starttls() 

            # Iniciar sesion con el correo electronico
            server.login(correo_remitente, contrasena_correo) 

            # se envia el mensaje por correo 
            server.send_message(mensaje) 

            # se cierra la conexion del servidor 
            server.quit()

            print('Correo electronico enviado con exito')

        except smtplib.SMTPException as e:
            print ('Error al intentar enviar el correo electronico, cuasa del error: ', e)