import sqlite3
from DATOS import base_datos as bd

class Persona:
    def __init__(self, usuario, contraseña, ruta_fotos):
        self.usuario = usuario
        self.contraseña = contraseña
        self.ruta_fotos = ruta_fotos

def create_table():
    conn = bd.conectar_db()
    c = conn.cursor()

    c.execute('''CREATE TABLE Persona (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario VARCHAR(50) NOT NULL,
                    contraseña VARCHAR(50) NOT NULL,
                    ruta_fotos VARCHAR(255)
                )''')
    bd.comit_cerrar_conexion(conn)

def insert(self, usuario:str, contraseña:str):
    #Persona(usuario, contraseña)
    conn = bd.conectar_db()
    c = conn.cursor()
    c.execute('''INSERT INTO Persona (usuario, contraseña) VALUES (?, ?)''', (usuario, contraseña))
    bd.comit_cerrar_conexion(conn)