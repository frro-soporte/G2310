from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.lang import Builder
from CONTROLADOR import controlador


class UI(ScreenManager):
    pass
    def reset_text(self):
        self.ids.nombre.text = ""
        self.ids.apellido.text = ""
        self.ids.dni.text = ""
        self.ids.mail.text = ""

    def AgregarEmpleado(self):
        nombrex = self.ids.nombre.text
        apellidox = self.ids.apellido.text
        dnix = self.ids.dni.text
        mailx = self.ids.mail.text
        controlador.insert( nombrex, apellidox, dnix, mailx)

class MyApp(App):
    def build(self):
        Window.size = (350, 500)
        Builder.load_file("D:/Soporte/practicos/G2310/TPIKIVY/UI/style.kv")
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