import sqlite3
from DATOS import base_datos as bd

def create_table():
    conn = bd.conectar_db()
    c = conn.cursor()

    c.execute('''CREATE TABLE Empleado (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre CHAR(30),
                    apellido CHAR(30),
                    dni INTEGER,
                    mail CHAR(30)
                )''')
    bd.comit_cerrar_conexion(conn)

def insert(self, nombre:str, apellido:str, dni:int, mail:str):
    Empleado(nombre, apellido, dni, mail)
    conn = bd.conectar_db()
    c = conn.cursor()
    c.execute('''INSERT INTO Empleado (nombre, apellido, dni, mail) VALUES (?, ?, ?, ?)''', (nombre, apellido, dni, mail))
    bd.comit_cerrar_conexion(conn)