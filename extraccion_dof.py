from ast import Try
from weber_dao import manipulacion_bd

from tkinter import *
from prueba_gifs import aparecer_gifs
import urllib.request
from datetime import datetime
from msilib.schema import Property
from bs4 import BeautifulSoup
import re 
'''
    importamos para envios de correos
'''
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

    def __init__(self):
        self.lst_nva_pub2=[]
        self.keyword = ''
        
        
    def acceso_web(self):
        '''
        Función que establece la conexion con la página,
        leerá y decodificará la página 
        '''
        lbl1 = Label(text="Conexion a la pagina web")
        lbl1.grid(row=2,column=1,padx=1, pady=4, ipadx=20,ipady=3)
        aparecer_gifs.aparecer_mensaje_2()

        # manipulacion = manipulacion_bd()
             
        url1 = manipulacion_bd.url_usado()

        print(url1)
        
        self.datos = urllib.request.urlopen(url1).read().decode()
            
           
    def buscar_69b(self):
        '''
        Función para transformar todo el HTML en un objeto de Beautiful Soup,
        busca dentro de las etiquetas la palabra clave y hace un conteo de las veces que aparece
        
        '''
        self.soup = BeautifulSoup(self.datos, 'lxml')
        self.box = self.soup.find('tr',id="trcontent")
        self.resultado = self.box.find_all('a',class_='enlaces')
        self.keyword = manipulacion_bd.palabra_usada()
        self.palabra = re.findall(self.keyword, str(self.resultado))
        
        lbl2 = Label(text="Obteniendo código fuente")
        lbl2.grid(row=3,column=1,padx=1, pady=4, ipadx=20,ipady=3)
        lbl3 = Label(text="Buscando palabra clave")
        lbl3.grid(row=4,column=1,padx=1, pady=4, ipadx=20,ipady=3)

        aparecer_gifs.aparecer_mensaje_3()
        
        #print(self.palabra)
        
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
        lst_link_dominio =[]
        x=0
    
        lbl4 = Label(text="Extrayendo links de publicaciones...")
        lbl4.grid(row=5,column=1,padx=1, pady=4, ipadx=20,ipady=3)

        aparecer_gifs.aparecer_mensaje_4()


        for ref in self.resultado:
            tag=ref.get('href')+'\n'
            transforma="".join(map(str, tag))
            link=[transforma.split('\n')]
            self.lst_links.append(link)
            
        #Resguarda especialmente los links en donde se encuentre la palabra 69-B en una lista -lst_69B[]        
        for Pos_info in self.resultado:
            encuentra = re.findall(self.keyword, str(Pos_info))
            if bool(encuentra)==True:
                PosLink = self.lst_links[x]
                self.lst_69B.append(PosLink)
            
            x+=1

        #Elimina carcateres innecesarios de los links y las concatena con el dominio de la pagina 
        for Textlink in self.lst_69B:
            cadena = Textlink[0]
            characters = "[]'"
            cadena = ''.join( x for x in cadena if x not in characters)
            dominio = manipulacion_bd.dominio_usado()
            cal=dominio+cadena
            lst_link_dominio.append(cal)
            print(cal)
        
        return lst_link_dominio
            

    def fecha_actual(self):
        '''
        Función para obtener la fecha actual
        '''
        today = datetime.now()
        
        return today
      
      
    def validar_pub_nva(self):
        '''
        Función que valida si los links encontrados no se encuentran en la base de datos y 
        sean considerados como nuevas publicaciones
        '''
        # Validar si la publiacion es nueva o ya ha sido almacenada en la base de datos
        # self.cont_link_dominio = 0
        self.cont_link_dominio = 0
        self.lst_nva_pub = []
        self.cont_lig = 0
        lst_link_dominio = self.obtener_link()
        # today = datetime.now()
        # self.valores = ()
        
        for ciclo in range(self.conteo):
            
            self.lst_nva_pub2 = manipulacion_bd.consulta_links(self, self.lst_nva_pub, self.cont_link_dominio, lst_link_dominio)
            self.cont_link_dominio+=1
        
        #Insercion de valores en la base de datos
        for ciclo in self.lst_nva_pub2:
            manipulacion_bd.insertar_links(self, self.lst_nva_pub2, self.fecha_actual(), self.cont_lig)
            self.cont_lig+=1
        
        
        label = Label(text="Guardando links en la base de datos")
        label.grid(row=3,column=3,padx=1, pady=4, ipadx=20,ipady=3)
        aparecer_gifs.aparecer_mensaje_6()
        

        # Convertimos la lista de los links nuevos en cadena de texto
        self.str_pubs_nva = ", \n ".join(self.lst_nva_pub2)
        # print(f"links encontrados{self.str_pubs_nva}")

    def notificacion_correo(self):
        '''
        Función que envia notificacion por correo electronico 
        cuando termina de realizar la consulta en la página del DOF
        '''
        self.asunto_correo = "Publicaciones del Diario Oficial de la Federación" 
        self.correo_remitente = "frester_dui98@hotmail.com" 
        # self.correo_remitente = "jnahuat@nasa.com.mx"
        self.correo_receptor = "oaguilar@nasa.com.mx"
        # self.correo_receptor = "frester_dui98@hotmail.com"
        self.email_smtp = "smtp.office365.com" 
        # self.contrasena_correo = "stkqsdfppwkxgtnml"
        # self.contrasena_correo = "stckrhhmhjxfqwgl" #contraseña aplicacion Nasa
        self.contrasena_correo = "poykyzptkdiihjhe" #contraseña aplicacion hotmail frester
        
        self.mensaje = EmailMessage() 
        self.mensaje['Subject'] = self.asunto_correo 
        self.mensaje['From'] = self.correo_remitente 
        self.mensaje['To'] = self.correo_receptor
                
        if bool(self.lst_nva_pub2) == True:
            # Mensaje de texto que se enviará
            print(f"Se ha identificado una nueva publicación referente al artículo 69-B: \n{self.str_pubs_nva}")
            self.mensaje.set_content(f"Se ha identificado una nueva publicación referente al artículo 69-B: \n{self.str_pubs_nva}") 

            lbl5 = Label(text="Conectando al servidor SMTP")
            lbl5.grid(row=1,column=3,padx=1, pady=4, ipadx=20,ipady=3)

            lbl6 = Label(text="Correo electrónico enviado con éxito")
            lbl6.grid(row=2,column=3,padx=1, pady=4, ipadx=20,ipady=3)

            aparecer_gifs.aparecer_mensaje_5()
            try:
                # smtp servidor y puerto 
                server = smtplib.SMTP('smtp.office365.com', port=587) 
                server.ehlo() 
                server.starttls() 
                #print("Conectando al servidor SMTP")

                server.login(self.correo_remitente, self.contrasena_correo) 
                server.send_message(self.mensaje) 
                server.quit()

                #print('Correo electronico enviado con exito')

                
            except smtplib.SMTPException as e:
                print ('Error al intentar enviar el correo electronico, cuasa del error: ', e)

        if bool(self.lst_nva_pub2) == False:
            print("No se ha encontrado publicación nueva referente al articulo 69-B")
            self.mensaje.set_content("No se ha encontrado publicación nueva referente al articulo 69-B") 

            lbl5 = Label(text="Conectando al servidor SMTP")
            lbl5.grid(row=1,column=3,padx=1, pady=4, ipadx=20,ipady=3)
            lbl6 = Label(text="Correo electrónico enviado con éxito")
            lbl6.grid(row=2,column=3,padx=1, pady=4, ipadx=20,ipady=3)

            aparecer_gifs.aparecer_mensaje_5()
            
            try:
                server = smtplib.SMTP('smtp.office365.com', port=587)  
                server.ehlo() 
                server.starttls() 
                #print("Conectando al servidor SMTP")

                server.login(self.correo_remitente, self.contrasena_correo) 
                server.send_message(self.mensaje) 
                server.quit()
                
                #print('Correo electronico enviado con exito')


            except smtplib.SMTPException as e:
                print ('Error al intentar enviar el correo electronico, cuasa del error: ', e)