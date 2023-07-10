import sqlite3
from DATOS import clases as cl

"""def conectar_db():
    conn = sqlite3.connect('D:/Soporte/practicos/G2310/TPIKIVY/base_datos_kivy.db')
    return conn

def comit_cerrar_conexion(conn):
    conn.commit()
    conn.close()"""

def create_table():
    cl.create_table()

def validar_dni(self, dni):
    return cl.validar_dni(self,dni)

def insert(self, nombre:str, apellido:str, dni:int, mail:str):
    cl.insert(self, nombre, apellido, dni, mail)
    