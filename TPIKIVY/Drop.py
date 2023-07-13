from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
from kivy.lang import Builder


Builder.load_string("""
<CustomDropDown>
    Button:
        text: 'Opción 1'
        size_hint_y: None
        height: 44
        on_release: app.show_popup(self.text)

    Button:
        text: 'Opción 2'
        size_hint_y: None
        height: 44
        on_release: app.show_popup(self.text)

    Button:
        text: 'Opción 3'
        size_hint_y: None
        height: 44
        on_release: app.show_popup(self.text)

    Button:
        text: 'Opción 4'
        size_hint_y: None
        height: 44
        on_release: app.show_popup(self.text)

""")


class CustomDropDown(DropDown):
    pass


class MyApp(App):
    def build(self):
        
        self.mainbutton = Button(text="Seleccionar opción",
                                 size_hint=(0.5, 0.1),
                                 pos_hint={'center_x':0.5,'center_y':0.5})
        dropdown = CustomDropDown()

        self.mainbutton.bind(on_release=dropdown.open)

        dropdown.bind(on_select = self.select_text)

        return self.mainbutton
   
    def select_text(self,instance,x):
        self.mainbutton.text = x


    def show_popup(self, option):
        content = Button(text=f'Usted selecciono la opcion: {option}')
        popup = Popup(title='Selección', content=content, size_hint=(None, None), size=(400, 200))
        content.bind(on_release=popup.dismiss)
        popup.open()


if __name__ == '__main__':
    MyApp().run()





