from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from DATOS import clases as cl
from DATOS import base_datos as bd
from CONTROLADOR import limpiar as li
from UI import popup as po
import sqlite3

#VALIDACIONES
def validar_tabla():
    bd.validar_tabla()

class UI(ScreenManager):
    pass
    #POPUP
    def open_pop1(self):
        po.open_pop1(self)
    def open_pop2(self):
        po.open_pop2(self)
    def open_confirmar(self):
        po.open_confirmar(self)

    #LIMPIAR Y RESETS
    def error_vacios(self):
        return li.error_vacios(self)
    def reset_text_buscar(self, nombre_buscado, apellido_buscado, dni_buscado, mail_buscado):
        return li.reset_text_buscar(self, nombre_buscado, apellido_buscado, dni_buscado, mail_buscado)
    def reset_text_agregar(self, nombre_agregar, apellido_agregar, dni_agregar, mail_agregar):
        return li.reset_text_agregar(self, nombre_agregar, apellido_agregar, dni_agregar, mail_agregar)

    #VALIDACIONES
    def validardni(self):
        dnix = self.ids.dni_agregar.text
        result = cl.validar_dni(self, dnix)
        return result
    
    #CREAR
    def AgregarEmpleado(self,state):
        if state == True:
            nombrex = self.ids.nombre_agregar.text
            apellidox = self.ids.apellido_agregar.text
            dnix = self.ids.dni_agregar.text
            mailx = self.ids.mail_agregar.text
            cl.insert(self, nombrex, apellidox, dnix, mailx)
        else:
            pass

    #BUSCAR
    def BuscarEmpleado(self):
        dni = self.ids.buscardni.text
        empleado = cl.search(self, dni)
        if empleado is not None:
            self.ids.nombre_buscado.text = empleado[1]
            self.ids.apellido_buscado.text = empleado[2]
            self.ids.dni_buscado.text = str(empleado[3])
            self.ids.mail_buscado.text = empleado[4]
            self.ids.nombre_sinbuscar.text = "Nombre:"
            self.ids.apellido_sinbuscar.text = "Apellido:"
            self.ids.dni_sinbuscar.text = "DNI:"
            self.ids.mail_sinbuscar.text = "Mail:"
            return True
        else:
            return False

    #ELIMINAR
    def EliminarEmpleado(self):
        dni_eli= self.ids.buscardni.text
        cl.delete(self, dni_eli)

#PRINCIPAL
class MyApp(App):
    def build(self):
        Window.size = (350, 500)
        Builder.load_file("../G2310/TPIKIVY/UI/style.kv")
        return UI()