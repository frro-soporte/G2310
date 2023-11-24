from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.filechooser import FileChooserListView
from deteccion import CameraScreen
from screen2 import LoginScreen
from screen1 import LoginScreen2

class IndexScreen(Screen):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.title = "INDEX"

            self.background_color = (0.2, 0.6, 1, 1)
            
            self.add_widget(Label(text="¡Bienvenidos!", pos_hint= {'center_x': 0.5, 'center_y': 0.95}))

            files_button = Button(
                text="Galería",
                size_hint= (0.40, 0.05),
                pos_hint= {'center_x': 0.5, 'center_y': 0.50 }
            )
            files_button.bind(on_press=self.go_to_files)
            self.add_widget(files_button)

            camera_button = Button(
                text="Cámara",
                size_hint= (0.40, 0.05),
                pos_hint= {'center_x': 0.5, 'center_y': 0.58 }
            )

            camera_button.bind(on_press=self.go_to_camera)
            self.add_widget(camera_button)
    
        def go_to_camera(self, instance):
            if "camera" not in self.manager.screen_names:
                self.manager.add_widget(CameraScreen(name="camera"))
            self.manager.current = "camera"

        def go_to_files(self, instance):
            self.manager.current = "files"

        def on_pre_enter(self):
            App.get_running_app().title = self.title


class FileScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Files Screen" 
        layout = BoxLayout(orientation='vertical')

        self.file_chooser = FileChooserListView(path='TPOPENCV', filters=['*.jpg', '*.png', '*.mp4'])
        layout.add_widget(self.file_chooser)

        self.media_widget = BoxLayout(orientation='vertical')
        layout.add_widget(self.media_widget)

        files_button = Button(text="Volver", size_hint=(0.20, 0.080), size = (100, 50), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        files_button.bind(on_press=self.go_to_index)
        layout.add_widget(files_button)

        self.add_widget(layout)

        self.file_chooser.bind(selection=self.load_media)


    def load_media(self, instance, value):
        self.media_widget.clear_widgets()

        selected = value  
        if selected:
            selected_file = selected[0]

            if selected_file.lower().endswith(('.jpg', '.png')):
                image_widget = Image(source=selected_file)
                self.media_widget.add_widget(image_widget)
            elif selected_file.lower().endswith('.mp4'):
                video_player = VideoPlayer(source=selected_file, state='play')
                self.media_widget.add_widget(video_player)

    def go_to_index(self, instance):
        self.manager.current = "index"

    def on_pre_enter(self):
        App.get_running_app().title = self.title


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen2(name="login"))
        sm.add_widget(IndexScreen(name="index"))
        sm.add_widget(FileScreen(name="files"))
        return sm


if __name__ == '__main__':
    MyApp().run()
