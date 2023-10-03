from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
import sqlite3

#VALIDACIONES
#ef validar_tabla():
#    bd.validar_tabla()

class UI(ScreenManager):
    pass
   
#PRINCIPAL
class MyApp(App):
    def build(self):
        Window.size = (350, 500)
        Builder.load_file("../G2310/TPOPENCV/UI/style.kv")
        return UI()