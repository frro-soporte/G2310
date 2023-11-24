from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.video import Video
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.filechooser import FileChooserListView

class MediaExplorerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        file_chooser = FileChooserListView(path='TPOPENCV/Galeria/Videos', filters=['*.jpg', '*.png', '*.mp4'])
        
        media_widget = BoxLayout(orientation='horizontal')
        media = None

        def load_media(instance, value):
            nonlocal media
            selected = value
            if selected:
                selected_file = selected[0]

                if selected_file.lower().endswith(('.jpg', '.png')):
                    
                    if media is not None:
                        media_widget.remove_widget(media)
                    media = Image(source=selected_file)
                elif selected_file.lower().endswith('.mp4'):
                   
                    if media is not None:
                        media_widget.remove_widget(media)
                    media = VideoPlayer(source=selected_file, state='play')

                media_widget.add_widget(media)

        file_chooser.bind(selection=load_media)

        layout.add_widget(file_chooser)
        layout.add_widget(media_widget)

        return layout

if __name__ == '__main__':
    MediaExplorerApp().run()
