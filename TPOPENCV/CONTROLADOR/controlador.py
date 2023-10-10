from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from UI import popup as po
import sqlite3
import cv2
from DATOS import base_datos as bd
from DATOS import clases as cl
from CONTROLADOR import CapaEntrada

#VALIDACIONES
def validar_tabla():
    bd.validar_tabla()

class UI(ScreenManager):
    pass
    def open_pop1(self):
        po.open_pop1(self)
    def open_confirmar(self):
        po.open_confirmar(self)

    def start_capture(self):
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0 / 30.0)

    def stop_capture(self):
        self.capture.release()
        Clock.unschedule(self.update)

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            user=self.ids.usuario_registrar.text
            #CapaEntrada.CapturarRostro(self.capture,frame,user)
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tostring()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.ids.registrar_image.texture = texture

    def AgregarPersona(self):
        usuario = self.ids.usuario_registrar.text
        contraseña = self.ids.pass_registrar.text
        cl.insert(self, usuario, contraseña)
        return usuario
    
    def capturar(self):
        user=self.ids.usuario_registrar.text
        CapaEntrada.CapturarRostro(user)
            
#PRINCIPAL
class MyApp(App):
    def build(self):
        Window.size = (350, 500)
        Builder.load_file("../G2310/TPOPENCV/UI/style.kv")
        return UI()