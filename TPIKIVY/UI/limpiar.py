def error_vacios(self):
    if (self.ids.nombre.text and self.ids.apellido.text and self.ids.dni.text and self.ids.mail.text) == "":
        return False
    else:
        return True
        
def reset_text(self, nombre_buscado, apellido_buscado, dni_buscado, mail_buscado):
    self.ids.nombre_buscado.text = ""
    self.ids.apellido_buscado.text = ""
    self.ids.dni_buscado.text = ""
    self.ids.mail_buscado.text = ""