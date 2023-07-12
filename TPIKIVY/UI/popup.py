from kivy.uix.popup import Popup

class MyPopup1(Popup):
    pass
class MyPopup2(Popup):
    pass
class Confirmar(Popup):
    pass
    def __init__(self, tipo, dni, **kwargs):
          super(Confirmar, self).__init__(**kwargs)
          self.tipo = tipo
          self.dni = dni
def open_pop1(self):
        pops = MyPopup1()
        pops.open()

def open_pop2(self):
        pops = MyPopup2()
        pops.open()

def open_confirmar(self, tipo, dni):
        pops = Confirmar(tipo, dni)
        pops.open()