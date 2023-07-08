from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.lang import Builder


class UI(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        Window.size = (350, 500)
        Builder.load_file("style.kv")
        return UI()
    
MyApp().run()