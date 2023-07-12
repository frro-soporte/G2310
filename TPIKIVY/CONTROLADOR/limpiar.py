def error_vacios(self):
    if (self.ids.nombre_agregar.text == "") and (self.ids.apellido_agregar.text == "") and (self.ids.dni_agregar.text == "") and (self.ids.mail_agregar.text == ""):
        return False
    else:
        return True
        
def reset_text_buscar(self, nombre_buscado, apellido_buscado, dni_buscado, mail_buscado):
    self.ids.nombre_buscado.text = ""
    self.ids.apellido_buscado.text = ""
    self.ids.dni_buscado.text = ""
    self.ids.mail_buscado.text = ""

def reset_text_agregar(self, nombre_agregar, apellido_agregar, dni_agregar, mail_agregar):
    self.ids.nombre_agregar.text = ""
    self.ids.apellido_agregar.text = ""
    self.ids.dni_agregar.text = ""
    self.ids.mail_agregar.text = ""