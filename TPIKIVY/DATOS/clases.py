import sqlite3
from DATOS import base_datos as bd
class Empleado:
    def __init__(self, nombre:str, apellido:str, dni:int, mail:str) -> None:
        pass 
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.mail = mail

def validar_dni(self, dni):
    conn = bd.conectar_db()
    c = conn.cursor()
    c.execute("SELECT dni FROM Empleado WHERE dni = ?", dni)
    result = c.fetchone()
    if result is None:
        bd.comit_cerrar_conexion(conn)
        return True  
    else:
        bd.comit_cerrar_conexion(conn)
        return False

def create_table():
    conn = bd.conectar_db()
    c = conn.cursor()

    c.execute('''CREATE TABLE Empleado (
                    nombre CHAR(30),
                    apellido CHAR(30),
                    dni INTEGER PRIMARY KEY,
                    mail CHAR(30)
                )''')
    bd.comit_cerrar_conexion(conn)

def insert(self, nombre:str, apellido:str, dni:int, mail:str):
    Empleado(nombre, apellido, dni, mail)
    conn = bd.conectar_db()
    c = conn.cursor()
    c.execute('''INSERT INTO Empleado (nombre, apellido, dni, mail) VALUES (?, ?, ?, ?)''', (nombre, apellido, dni, mail))
    bd.comit_cerrar_conexion(conn)



        
