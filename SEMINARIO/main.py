import pandas as pd
import os
pd.set_option('display.float_format', '{:.2f}'.format)
ruta_archivo = "D:\\Usuarios\\Martin\\Escritorio\\Soporte\\ventas3.xlsx"
df = pd.read_excel(ruta_archivo)

def MostrarDatos(df):
    with open("output.txt", "w") as f:
        f.write(df.to_string())
    os.system("output.txt")
    
def series():
    #####CREAR SERIE A PARTIR DE UNA LISTA Y INGRESANDO LOS INDICES COMO PARAMETROS
    serie = pd.Series([15, 12, 21], index=["Enero", "Febrero", "Marzo"])
    print(serie)

def dataframes():
    #####CREAR DATAFRAME
    data = {
    'Nombre': ['Juan', 'María', 'Pedro', 'Ana'],
    'Edad': [25, 30, 22, 28],
    'Ciudad': ['Rosario', 'Charata', 'Madrid', 'Sevilla']
    }
    df = pd.DataFrame(data)
    print(df)

def filtrado_seleccion():
    #####Consultar la columna FechaPedido
    df = df["FechaPedido"]
    #####Seleccionar la primera fila
    #df = df.loc[0]
    #####Consultar los pedidos en el año 2020
    #df = df[df["FechaPedido"].dt.year == 2020]
    MostrarDatos(df)

def faltantes():
    #####Comprobar columna Null
    df= df.isnull()
    #####Descartar valores nulos
    #df = df.dropna(axis=1)
    #####Rellenar celdas vacias con un valor
    #df = df.fillna(value="-")
    MostrarDatos(df)

def operaciones():
    columna_interes = ["PrecioUnitario", "CostoUnitario", "ImporteVentaTotal", "ImporteCostoTotal"]
    #####Agrupar por zona mostrando las analiticas descriptivas de las columnas de interes
    df = df.groupby("Zona")[columna_interes].describe().transpose()
    #####Consultar cual fue la venta mas chica en unidades
    #df = df.loc[df["Unidades"].idxmin()]
    #####Consultar cual fue la venta mas grande en unidades
    #df = df.loc[df["Unidades"].idxmax()]
    #####Consultar las primeras 5 filas
    #df = df.head()
    #####Consultar las ultimas 5 filas
    #df = df.tail()
    #####Consultar las datos unicos
    #df = df["Zona"].value_counts()
    #####Aplicar una funcion a la columna CostoUnitario
    #df["CostoUnitario"] = df["CostoUnitario"].apply(lambda x: x + 10)
    #df["ImporteCostoTotal"] = df["CostoUnitario"] * df["Unidades"]
    ######Ordenar por unidades de menor a mayor
    #df = df.sort_values(by="Unidades",ascending=True)
    ######Ordenar por fecha reciente
    #df = df.sort_values(by="FechaPedido",ascending=False)
    ######Agregar una columna "Ganancia" que es la diferencia de "ImporteCostoTotal" * "ImporteVentaTotal"
    #df["Ganancia"] = df["ImporteVentaTotal"] - df["ImporteCostoTotal"]
    ######Borrar la columna "Null"
    #df = df.drop("Null",axis=1)
    MostrarDatos(df)
    



#series()
#dataframes()
#filtrado_seleccion()
#faltantes()
#operaciones()