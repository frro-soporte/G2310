"""Base de Datos - Creación de Clase en ORM"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine("sqlite:///practico_05/socios.db", echo = True)
Base = declarative_base()

class Socio(Base):
    """Implementar un modelo Socio a traves de Alchemy que cuente con los siguientes campos:
        - id_socio: entero (clave primaria, auto-incremental, unico)
        - dni: entero (unico)
        - nombre: string (longitud 250)
        - apellido: string (longitud 250)
    """
    __tablename__ = 'socios'
    id_socio = Column(Integer(), primary_key=True)
    dni = Column(Integer())
    nombre = Column(String(250))
    apellido =Column(String(250))

    def __str__(self):
        return self.dni

Session = sessionmaker(engine)
session = Session()

"""if __name__ == "__main__":
    Base.metadata.create_all(engine)
    session.close()"""

