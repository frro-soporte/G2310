import sqlite3
from DATOS import clases as cl
from DATOS import base_datos as bd

def validar_dni(self, dni):
    return cl.validar_dni(self,dni)

def validar_tabla():
    bd.validar_tabla()

def insert(self, nombre:str, apellido:str, dni:int, mail:str):
    cl.insert(self, nombre, apellido, dni, mail)
    