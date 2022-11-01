from ast import Try
from weber_dao import *

import urllib.request
from datetime import datetime
from msilib.schema import Property
from bs4 import BeautifulSoup
import re 
'''importamos para envios de correos '''
import smtplib 
from email.message import EmailMessage 


'''
Documentar el código
try para errores de importacion 
archivo de requeriments 
agregar los self 
eliminar lineas inecesarias
documentar metodos 
asignar nombres de variables relacionadas a su funcion 
nombre de clase empieza en mayuscula
globales en mayusculas
uso de propiedades
nombre de los archivos 
formato de los snake case 
dos saltos de linea en cada def
'''


class extraccion():
    '''
    Clase que se utiliza para la extraccion de los links de la página del DOF
    '''

    def acceso_web(self):
        '''
        Función que establece la conexion con la página,
        leerá y decodificará la página 
        '''
        
        try:
            self.datos = urllib.request.urlopen("https://www.dof.gob.mx/index_111.php?year=2022&month=08&day=30#gsc.tab=0").read().decode()
            print("Conexion a la pagina web establecida")
        except urllib.error.URLerror as e:
            print(f"Error al intentar acceder a la pagina web: {e}")
            
    
    def buscar_69b(self):
        '''
        Función para transformar todo el HTML en un objeto de Beautiful Soup,
        busca dentro de las etiquetas la palabra clave y hace un conteo de las veces que aparece
        
        '''
        self.soup = BeautifulSoup(self.datos, 'lxml')
        self.box = self.soup.find('tr',id="trcontent")
        self.resultado = self.box.find_all('a',class_='enlaces')
        self.palabra = re.findall(r'69-B', str(self.resultado))
        print("Buscando palabra clave")
        print(self.palabra)
        
        #Contar elementos
        self.transforma = ", ".join(map(str, self.palabra))
        self.conteo = len(self.transforma.split())
        
        


    def obtener_link(self):
        '''
        Función que recupera los links de las las publicaciones donde se encuentre la palabra
        clave
        '''
        #Recupera todos los link de las publicaciones y las almacena en una lista -links[]
        self.lst_links =[]
        self.lst_69B =[]
        self.lst_link_dominio =[]
        x=0
        print ("Extrayendo links de publicaciones...")
        for ref in self.resultado:
            tag=ref.get('href')+'\n'
            transforma="".join(map(str, tag))
            link=[transforma.split('\n')]
            self.lst_links.append(link)
            
        #Resguarda especialmente los links en donde se encuentre la palabra 69-B en una lista -lst_69B[]        
        for Pos_info in self.resultado:
            encuentra = re.findall(r'69-B', str(Pos_info))
            if bool(encuentra)==True:
                PosLink = self.lst_links[x]
                self.lst_69B.append(PosLink)
            
            x+=1

        #Elimina carcateres innecesarios de los links y las concatena con el dominio de la pagina 
        for Textlink in self.lst_69B:
            cadena = Textlink[0]
            characters = "[]'"
            cadena = ''.join( x for x in cadena if x not in characters)
            cal='https://www.dof.gob.mx'+cadena
            self.lst_link_dominio.append(cal)
            print(cal)
            

    def fecha_actual(self):
        '''
        Función para obtener la fecha actual
        '''
        self.today = datetime.now()
        
        
    def validar_pub_nva(self):
        '''
        Función que valida si los links encontrados no se encuentran en la base de datos y 
        sean considerados como nuevas publicaciones
        '''
        # Validar si la publiacion es nueva o ya ha sido almacenada en la base de datos
        self.cont_link_dominio = 0
        self.lst_nva_pub=[]
        self.cont_lig = 0
        self.valores = ()
        
        for ciclo in range(self.conteo):
            consulta_links
            self.cont_link_dominio+=1

        #Insercion de valores en la base de datos
        for ciclo in self.lst_nva_pub:
            insertar_links
            self.cont_lig+=1
        
        

        # Convertimos la lista de los links nuevos en cadena de texto
        self.str_pubs_nva = ", \n ".join(self.lst_nva_pub)
        print(f"links encontrados{self.str_pubs_nva}")

    def notificacion_correo(self):
        '''
        Función que envia notificacion por correo electronico 
        cuando termina de realizar la consulta en la página del DOF
        '''
        self.asunto_correo = "Publicaciones del Diario Oficial de la Federación" 
        self.correo_remitente = "jnahuat@nasa.com.mx" 
        self.correo_receptor = "frester_dui98@hotmail.com"
        self.email_smtp = "smtp.office365.com" 
        self.contrasena_correo = "stckrhhmhjxfqwgl" #contraseña aplicacion Nasa
        #email_password = "poykyzptkdiihjhe" #contraseña aplicacion hotmail frester
        
        self.mensaje = EmailMessage() 
        self.mensaje['Subject'] = self.asunto_correo 
        self.mensaje['From'] = self.correo_remitente 
        self.mensaje['To'] = self.correo_receptor
                
        if bool(self.lst_nva_pub) == True:
            # Mensaje de texto que se enviará
            self.mensaje.set_content(f"Se ha identificado una nueva publicación referente al artículo 69-B: \n{self.str_pubs_nva}") 

            try:
                # smtp servidor y puerto 
                server = smtplib.SMTP('smtp.office365.com', port=587) 
                server.ehlo() 
                server.starttls() 
                print("Conectando al sservidor SMTP")
                server.login(self.correo_remitente, self.contrasena_correo) 
                server.send_message(self.mensaje) 
                server.quit()

                print('Correo electronico enviado con exito')
                
            except smtplib.SMTPException as e:
                print ('Error al intentar enviar el correo electronico, cuasa del error: ', e)

        if bool(self.lst_nva_pub) == False:
            self.mensaje.set_content("No se ha encontrado publicación nueva referente al articulo 69-B") 

            try:
                server = smtplib.SMTP('smtp.office365.com', port=587)  
                server.ehlo() 
                server.starttls() 
                print("Conectando al servidor SMTP")
                server.login(self.correo_remitente, self.contrasena_correo) 
                server.send_message(self.mensaje) 
                server.quit()
                
                print('Correo electronico enviado con exito')

            except smtplib.SMTPException as e:
                print ('Error al intentar enviar el correo electronico, cuasa del error: ', e)