import sqlite3
from DATOS import clases as cl

def validar_tabla():
    conn = conectar_db()
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Empleado'")
    result = c.fetchone()
    if result is None:
        cl.create_table()
        comit_cerrar_conexion(conn)


def conectar_db():
    conn = sqlite3.connect('../G2310/TPIKIVY/base_datos_kivy_2.db')
    return conn

def comit_cerrar_conexion(conn):
    conn.commit()
    conn.close()
