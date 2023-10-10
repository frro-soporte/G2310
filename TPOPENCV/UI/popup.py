from kivy.uix.popup import Popup

class MyPopup1(Popup):
    pass
class MyPopup2(Popup):
    pass
class Confirmar(Popup):
    pass
def open_pop1(self):
    pops = MyPopup1()
    pops.open()

def open_confirmar(self):
    pops = Confirmar()
    pops.open()
