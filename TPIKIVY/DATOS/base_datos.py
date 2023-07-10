import sqlite3
def conectar_db():
    conn = sqlite3.connect('D:/Soporte/practicos/G2310/TPIKIVY/base_datos_kivy.db')
    return conn

def comit_cerrar_conexion(conn):
    conn.commit()
    conn.close()
