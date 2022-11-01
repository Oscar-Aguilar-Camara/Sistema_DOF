from Base_datos_scrapper import conexion_bd

def consulta_links(self):
        conexion = conexion_bd()     
        conexion.cursor.execute("SELECT * FROM `extraccion` WHERE link = %s;", (self.lst_link_dominio[self.cont_link_dominio],))
        self.valores = self.fetchall()
        conexion.close_connection
        

def insertar_links(self):
        conexion = conexion_bd()  
        conexion.cursor.execute("INSERT INTO `extraccion` (`id`, `link`, `fecha`) VALUES (NULL,%(liga)s, %(fecha_actual)s)",{"liga":self.lst_nva_pub[self.cont_lig],"fecha_actual":self.today}) 
        conexion.close_connection