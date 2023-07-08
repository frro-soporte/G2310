"""Base de Datos SQL - Baja"""

import datetime
import sqlite3
from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona


def borrar_persona(id_persona:int):
    """Implementar la funcion borrar_persona, que elimina un registro en la 
    tabla Persona. Devuelve un booleano en base a si encontro el registro y lo 
    borro o no."""
    pass # Completar
    conn = sqlite3.connect('base_datos.db')
    c= conn.cursor()

    c.execute("SELECT * FROM Persona WHERE IdPersona = ?", (id_persona,))
    registro = c.fetchone()

    if registro is not None:
        c.execute('DELETE FROM Persona WHERE IdPersona = ?', (id_persona,))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False

# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
