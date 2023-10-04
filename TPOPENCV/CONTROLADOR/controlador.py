from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import sqlite3
import cv2

#VALIDACIONES
#ef validar_tabla():
#    bd.validar_tabla()

class UI(ScreenManager):
    pass
    def start_capture(self):
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0 / 30.0)

    def stop_capture(self):
        self.capture.release()
        Clock.unschedule(self.update)

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tostring()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.ids.camera_image.texture = texture
#PRINCIPAL
class MyApp(App):
    def build(self):
        Window.size = (350, 500)
        Builder.load_file("../G2310/TPOPENCV/UI/style.kv")
        return UI()