from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from CONTROLADOR import controlador

class MyPopup1(Popup):
    pass
class MyPopup2(Popup):
    pass


class UI(ScreenManager):
    pass
    def open_pop1(self):
        pops = MyPopup1()
        pops.open()

    def open_pop2(self):
        pops = MyPopup2()
        pops.open()

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

    def validardni(self):
        dnix = self.ids.dni.text
        result = controlador.validar_dni(self, dnix)
        return result
    
    def AgregarEmpleado(self):
        nombrex = self.ids.nombre.text
        apellidox = self.ids.apellido.text
        dnix = self.ids.dni.text
        mailx = self.ids.mail.text
        controlador.insert(self, nombrex, apellidox, dnix, mailx)

    def BuscarEmpleado(self):
        dni = self.ids.buscardni.text
        empleado = controlador.search(self, dni)
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

    def EliminarEmpleado(self):
        dni_eli= self.ids.buscardni.text
        controlador.delete(self, dni_eli)

class MyApp(App):
    def build(self):
        Window.size = (350, 500)
        Builder.load_file("../G2310/TPIKIVY/UI/style.kv")
        return UI()