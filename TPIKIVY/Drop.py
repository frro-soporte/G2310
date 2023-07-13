from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.lang import Builder


Builder.load_string("""
<CustomDropDown>
    Button:
        text: 'Opción 1'
        size_hint_y: None
        height: 44
        on_release: root.select('Opcion 1')


    Button:
        text: 'Opción 2'
        size_hint_y: None
        height: 44
        on_release: root.select('Opcion 2')


    Button:
        text: 'Opción 3'
        size_hint_y: None
        height: 44
        on_release: root.select('Opcion 3')


    Button:
        text: 'Opción 4'
        size_hint_y: None
        height: 44
        on_release: root.select('Opcion 4')


    Button:
        text: 'Opción 5'
        size_hint_y: None
        height: 44
        on_release: root.select('Opcion 5')
""")


class CustomDropDown(DropDown):
    pass


class MyApp(App):
    def build(self):
        #Window.size = (350, 500)
        mainbutton = Button(text='Seleccionar opción',
                                 size_hint=(0.5, 0.1),
                                 pos_hint=(None,None))
        dropdown = CustomDropDown()


        # Crear los botones del menú
        #for i in range(1, 6):
            #btn = Button(text=f'Opción {i}', size_hint_y=None, height=40)
            #btn.bind(on_release=lambda btn: self.show_popup(btn.text))
            #dropdown.add_widget(btn)
           
        mainbutton.bind(on_release=dropdown.open)


        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))


        #dropdown.bind(on_select = self.select_text)


       # main_layout.add_widget(main_button)


        return mainbutton
   
    #def select_text(self,instance,x):
        #self.mainbutton.text = x


    #def show_popup(self, option):
        #content = Button(text=f'Opción seleccionada: {option}')
        #popup = Popup(title='Selección', content=content, size_hint=(None, None), size=(400, 200))
        #content.bind(on_release=popup.dismiss)
        #popup.open()


if __name__ == '__main__':
    MyApp().run()





