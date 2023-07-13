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
    def open_confirmar(self, tipo, dni):
        po.open_confirmar(self, tipo, dni)

    #LIMPIAR Y RESETS
    def error_vacios(self):
        return li.error_vacios(self)
    def reset_text(self, state):
        return li.reset_text(self, state)

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
    def BuscarEmpleado(self,dni,state):
        empleado = cl.search(self, dni)
        if empleado is not None:
            if state == "eliminar":
                self.ids.nombre_buscado_eliminar.text = empleado[1]
                self.ids.apellido_buscado_eliminar.text = empleado[2]
                self.ids.dni_buscado_eliminar.text = str(empleado[3])
                self.ids.mail_buscado_eliminar.text = empleado[4]
                self.ids.nombre_sinbuscar_eliminar.text = "Nombre:"
                self.ids.apellido_sinbuscar_eliminar.text = "Apellido:"
                self.ids.dni_sinbuscar_eliminar.text = "DNI:"
                self.ids.mail_sinbuscar_eliminar.text = "Mail:"
            elif state == "actualizar":
                self.ids.nombre_buscado_actualizar.disabled = False
                self.ids.nombre_buscado_actualizar.background_color = (1,1,1,1)
                self.ids.apellido_buscado_actualizar.disabled = False
                self.ids.apellido_buscado_actualizar.background_color = (1,1,1,1)
                self.ids.dni_buscado_actualizar.background_color = (1,1,1,1)
                self.ids.mail_buscado_actualizar.disabled = False
                self.ids.mail_buscado_actualizar.background_color = (1,1,1,1)
                self.ids.nombre_buscado_actualizar.text = empleado[1]
                self.ids.apellido_buscado_actualizar.text = empleado[2]
                self.ids.dni_buscado_actualizar.text = str(empleado[3])
                self.ids.mail_buscado_actualizar.text = empleado[4]
                self.ids.nombre_sinbuscar_actualizar.text = "Nombre:"
                self.ids.apellido_sinbuscar_actualizar.text = "Apellido:"
                self.ids.dni_sinbuscar_actualizar.text = "DNI:"
                self.ids.mail_sinbuscar_actualizar.text = "Mail:"
            elif state == "mostrar":
                self.ids.id_buscado_mostrar.text = str(empleado[0])
                self.ids.nombre_buscado_mostrar.text = empleado[1]
                self.ids.apellido_buscado_mostrar.text = empleado[2]
                self.ids.dni_buscado_mostrar.text = str(empleado[3])
                self.ids.mail_buscado_mostrar.text = empleado[4]
                self.ids.id_sinbuscar_mostrar.text = "id:"
                self.ids.nombre_sinbuscar_mostrar.text = "Nombre:"
                self.ids.apellido_sinbuscar_mostrar.text = "Apellido:"
                self.ids.dni_sinbuscar_mostrar.text = "DNI:"
                self.ids.mail_sinbuscar_mostrar.text = "Mail:"
            return True
        else:
            return False

    #ELIMINAR
    def disabled_eliminar(self):
            self.ids.boton_eliminar.disabled = False
    def EliminarEmpleado(self, dni, state):
        if state == True:
            cl.delete(self, dni)
        else:
            pass
            return False

    #ACTUALIZAR
    def ActualizarEmpleado(self, dni):
        cl.update(self, dni)

    #MOSTRAR DATOS
    #def MostrarEmpleado(self,dni):
        #lista= cl.read(self,dni)
        
#PRINCIPAL
class MyApp(App):
    def build(self):
        Window.size = (350, 500)
        Builder.load_file("../G2310/TPIKIVY/UI/style.kv")
        return UI()