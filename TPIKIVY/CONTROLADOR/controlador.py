import sqlite3

def conectar_db():
    conn = sqlite3.connect('base_datos_kivy.db')
    return conn

def comit_cerrar_conexion(conn):
    conn.commit()
    conn.close()

def create_table():
    conn = conectar_db()
    c = conn.cursor()

    c.execute('''CREATE TABLE Empleado (
                nombre CHAR(30),
                apellido CHAR(30),
                dni INTEGER PRIMARY KEY,
                mail CHAR(30)
            )''')
    comit_cerrar_conexion(conn)

def insert(nombre:str, apellido:str, dni:int, mail:str):
    conn = conectar_db()
    c = conn.cursor()

    c.execute('''INSERT INTO Empleado (nombre, apellido, dni, mail) VALUES (?, ?, ?, ?)''', (nombre, apellido, dni, mail))
    comit_cerrar_conexion(conn)