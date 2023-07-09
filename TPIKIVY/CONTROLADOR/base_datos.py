import sqlite3

def conectar_db(c):
    conn = sqlite3.connect('base_datos.db')
    c= conn.cursor()

def cerrar_conexion(conn):
    conn.commit()
    conn.close()