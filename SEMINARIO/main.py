import pandas as pd

def leer_excel():
    ##CARGAR ARCHIVO Y CREAR DATAFRAME
    ruta_archivo = "D:\\Usuarios\\Martin\\Escritorio\\Soporte\\ventas3.xlsx"
    df = pd.read_excel(ruta_archivo)
    return df

def series():
    ##CREAR SERIE A PARTIR DE UNA LISTA Y INGRESANDO LOS INDICES COMO PARAMETROS
    serie = pd.Series([15, 12, 21], index=["Enero", "Febrero", "Marzo"])
    print(serie)

def dataframes():
    ##CREAR DATAFRAME
    data = {
    'Nombre': ['Juan', 'María', 'Pedro', 'Ana'],
    'Edad': [25, 30, 22, 28],
    'Ciudad': ['Rosario', 'Charata', 'Madrid', 'Sevilla']
    }
    df = pd.DataFrame(data)
    print(df)

def filtrado_seleccion():
    df = leer_excel()
    ##Consultar la columna Pais
    #print(df["Pais"])
    ##Consultar las unidades mayor a 1000
    print(df[df["Unidades"]>1000])


filtrado_seleccion()