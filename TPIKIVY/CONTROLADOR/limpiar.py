def error_vacios(self):
    if (self.ids.nombre_agregar.text == "") and (self.ids.apellido_agregar.text == "") and (self.ids.dni_agregar.text == "") and (self.ids.mail_agregar.text == ""):
        return False
    else:
        return True
        
def reset_text(self, state):
    if state == "eliminar":
        self.ids.buscardni_eliminar.text = ""
        self.ids.nombre_sinbuscar_eliminar.text = ""
        self.ids.apellido_sinbuscar_eliminar.text = ""
        self.ids.dni_sinbuscar_eliminar.text = ""
        self.ids.mail_sinbuscar_eliminar.text = ""
        self.ids.nombre_buscado_eliminar.text = ""
        self.ids.apellido_buscado_eliminar.text = ""
        self.ids.dni_buscado_eliminar.text = ""
        self.ids.mail_buscado_eliminar.text = ""
    elif state == "agregar":
        self.ids.nombre_agregar.text = ""
        self.ids.apellido_agregar.text = ""
        self.ids.dni_agregar.text = ""
        self.ids.mail_agregar.text = ""
    elif state =="actualizar":
        self.ids.nombre_buscado_actualizar.disabled = True
        self.ids.nombre_buscado_actualizar.background_color = (0,0,0,0)
        self.ids.apellido_buscado_actualizar.disabled = True
        self.ids.apellido_buscado_actualizar.background_color = (0,0,0,0)
        self.ids.dni_buscado_actualizar.background_color = (0,0,0,0)
        self.ids.mail_buscado_actualizar.disabled = True
        self.ids.mail_buscado_actualizar.background_color = (0,0,0,0)
        self.ids.buscardni_actualizar.text = ""
        self.ids.nombre_sinbuscar_actualizar.text = ""
        self.ids.apellido_sinbuscar_actualizar.text = ""
        self.ids.dni_sinbuscar_actualizar.text = ""
        self.ids.mail_sinbuscar_actualizar.text = ""
        self.ids.nombre_buscado_actualizar.text = ""
        self.ids.apellido_buscado_actualizar.text = ""
        self.ids.dni_buscado_actualizar.text = ""
        self.ids.mail_buscado_actualizar.text = ""
    elif state == "mostrar":
        self.ids.buscardni_mostrar.text = ""
        self.ids.nombre_sinbuscar_mostrar.text = ""
        self.ids.apellido_sinbuscar_mostrar.text = ""
        self.ids.dni_sinbuscar_mostrar.text = ""
        self.ids.mail_sinbuscar_mostrar.text = ""
        self.ids.nombre_buscado_mostrar.text = ""
        self.ids.apellido_buscado_mostrar.text = ""
        self.ids.dni_buscado_mostrar.text = ""
        self.ids.mail_buscado_mostrar.text = ""
