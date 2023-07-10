from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.popup import Popup
from CONTROLADOR import controlador

class MyPopup (Popup):
    pass


class UI(ScreenManager):
    pass
    def open_pop(self):
        pops = MyPopup()
        pops.open()

    def error_vacios(self):
        if (self.ids.nombre.text and self.ids.apellido.text and self.ids.dni.text and self.ids.mail.text) == "":
            return False
        else:
            return True
    
    def reset_text(self):
        self.ids.nombre.text = ""
        self.ids.apellido.text = ""
        self.ids.dni.text = ""
        self.ids.mail.text = ""

    def validardni(self):
        dnix = self.ids.dni.text
        result = controlador.validar_dni(self, dnix)
        if result == True:
            pass
            return True
        else:
            return False
    def AgregarEmpleado(self):
        nombrex = self.ids.nombre.text
        apellidox = self.ids.apellido.text
        dnix = self.ids.dni.text
        mailx = self.ids.mail.text
        controlador.insert(self, nombrex, apellidox, dnix, mailx)

class MyApp(App):
    def build(self):
        Window.size = (350, 500)
        Builder.load_file("D:/Soporte/practicos/G2310/TPIKIVY/UI/style.kv") #VER UBICACION DEL STYLE
        return UI()

    """def AgregarEmpleado(self):
        nombrex = self.ids.nombre.text
        apellidox = self.ids.apellido.text
        dnix = self.ids.dni.text
        mailx = self.ids.mail.text
        if nombrex is None:
            estado = False
        else:
            estado = True
        return estado"""