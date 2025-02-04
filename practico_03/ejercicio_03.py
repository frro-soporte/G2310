"""Dataclasses"""


class Persona:
    """Clase con los siguientes miembros:

    Atributos de instancia:
    - nombre: str
    - edad: int
    - sexo (H hombre, M mujer): str
    - peso: float
    - altura: float

    Métodos:
    - es_mayor_edad(): indica si es mayor de edad, devuelve un booleano.
    """

    # Completar
    def __init__(self, nombre:str = None, edad:int = None, sexo:str = None, peso:float = None, altura:float = None) -> None:
        pass
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def es_mayor_edad(self) -> bool:
        return self.edad >= 18

# NO MODIFICAR - INICIO
assert Persona("Juan", 18, "H", 85, 175.9).es_mayor_edad()
assert not Persona("Julia", 16, "M", 65, 162.4).es_mayor_edad()
# NO MODIFICAR - FIN


###############################################################################


from dataclasses import dataclass

@dataclass
class Persona:
    """Re-Escribir utilizando DataClasses"""

    # Completar
    nombre: str
    edad: int
    sexo: str
    peso: int
    altura: float

    def es_mayor_edad(self) -> bool:
        return self.edad >=18

# NO MODIFICAR - INICIO
assert Persona("Juan", 18, "H", 85, 175.9).es_mayor_edad()
assert not Persona("Julia", 16, "M", 65, 162.4).es_mayor_edad()
# NO MODIFICAR - FIN
