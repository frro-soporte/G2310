import cv2

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import datetime
import os

from identidad import validar_identidad 

class LoginScreen2(Screen):
    log_in = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Log In"  

        self.label = Label(text="Iniciar Sesion o Registrarse", size_hint_y=None, pos_hint= {'center_x': 0.5, 'top': 0.98}, height=30)
        self.add_widget(self.label)
        
        self.capture = cv2.VideoCapture(0)
        self.image = Image(size_hint= (0.70, 0.70), pos_hint= {"center_x": 0.5, "center_y": 0.55})
        self.add_widget(self.image)

        login_button = Button(text="Ingresar", size_hint=(0.15, 0.05), pos_hint= {'center_x': 0.5, 'center_y': 0.12 })
        login_button.bind(on_press=self.capture_validate_image)
        self.add_widget(login_button)

        login_button = Button(text="Todavia no tenes cuenta? Registrarse", size_hint=(0.35, 0.05), pos_hint= {'center_x': 0.5, 'center_y': 0.060})
        login_button.bind(on_press=self.create_user)
        self.add_widget(login_button)

        Clock.schedule_interval(self.update, 1.0 / 30.0)

    def update(self, dt):

        ret, frame = self.capture.read()

        if ret:
            frame = cv2.flip(frame, 1)
            buf = cv2.flip(frame, 0).tostring()
            texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.image.texture = texture1

        if self.log_in:
            print("LOG IN")
            self.on_stop()
            self.go_to_index()

    
    def capture_validate_image(self, instance):
        self.label.text = "Validando"

        ret, frame = self.capture.read()
        if ret:
            cv2.imwrite("TPOPENCV_2/captura.jpg", frame)

        try:
            self.log_in = validar_identidad()
            if not self.log_in:
                self.label.text = "Usuario no encontrado."

        except Exception as e:
            print(e)

    
    def create_user(self, instance):

        folder_path= "TPOPENCV_2/Caras"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        now = datetime.datetime.now()
        date_time_str = now.strftime("%Y-%m-%d_%H-%M-%S")

        ret, frame = self.capture.read()
        if ret:
            cv2.imwrite("TPOPENCV_2/Caras/"+date_time_str+".jpg", frame)
            self.label.text = "Usuario creado"

    def go_to_index(self):
        self.manager.current = "index"

    def on_pre_enter(self):
        App.get_running_app().title = self.title

    def on_stop(self):
        self.capture.release()
        Clock.unschedule(self.update)

