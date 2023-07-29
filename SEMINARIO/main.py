import pandas as pd
import os
import matplotlib.pyplot as plt
pd.set_option('display.float_format', '{:.2f}'.format)

def leer_excel(archivo):
    ruta_archivo = "D:\\Soporte\\practicos\\G2310\\SEMINARIO\\ventas.xlsx"
    if archivo == "ventas":
        df = pd.read_excel(ruta_archivo, sheet_name="ventas")
    elif archivo == "concatenacion":
        indice = [1001, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009]
        df = pd.read_excel(ruta_archivo, sheet_name="concatenacion")
        #dfconc.set_index(pd.Series(indice), inplace=True)
    elif archivo == "fusion":
        df = pd.read_excel(ruta_archivo)
        df = pd.read_excel(ruta_archivo, sheet_name="fusion")
    elif archivo == "union":
        df = pd.read_excel(ruta_archivo)
        df = pd.read_excel(ruta_archivo, sheet_name="union")
    return df

def MostrarDatos(df):
    with open("D:\\Soporte\\practicos\\G2310\\SEMINARIO\\output.txt", "w") as f:
        f.write(df.to_string())
    os.system("D:\\Soporte\\practicos\\G2310\\SEMINARIO\\output.txt")
    
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

def filtrado_seleccion(df):
    #####Consultar la columna FechaPedido
    df = df["FechaPedido"]
    #####Seleccionar la primera fila
    #df = df.loc[0]
    #####Consultar los pedidos en el año 2020
    #df = df[df["FechaPedido"].dt.year == 2020]
    return df

def faltantes(df):
    #####Comprobar columna Null
    df= df.isnull()
    #####Descartar valores nulos
    #df = df.dropna(axis=1)
    #####Rellenar celdas vacias con un valor
    #df = df.fillna(value="-")
    return df

def operaciones(df):
    columna_interes = ["PrecioUnitario", "CostoUnitario", "ImporteVentaTotal", "ImporteCostoTotal"]
    #####Agrupar por zona mostrando las analiticas descriptivas de las columnas de interes
    df = df.groupby("Zona")[columna_interes].describe().transpose()
    #####Consultar cual fue la venta mas chica en unidades
    #df = df.loc[df["Unidades"].idxmin()]
    #####Consultar cual fue la venta mas grande en unidades
    #df = df.loc[df["Unidades"].idxmax()]
    return df

def transformacion(df):
    #####Consultar las primeras 5 filas
    df = df.head()
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
    return df

def combinaciones(df):
    ######Concatenacion con ventas en Sudamerica
    indices = [10010, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009]
    dfconc = leer_excel("concatenacion")
    dfconc.index = indices
    df = pd.concat([df,dfconc])
    ######Fusionar con la columna IDPedido para consultar si se termino de cobrar o sigue cobrando cuotas
    #dffus = leer_excel("fusion")
    #df = pd.merge(df, dffus, on="IDPedido")
    ######Union mediante indices para conocer el personal que estuvo a cargo del pedido
    #dfun = leer_excel("union")
    #df = df.join(dfun)
    return df

def MostrarGrafico(df):
    ######Muestra grafico de lineas de las cantidades de pedidos por año
    df["MesPedido"] = df["FechaPedido"].dt.month
    df["AñoPedido"] = df["FechaPedido"].dt.year
    dfgraf1 = df.groupby(["AñoPedido", "MesPedido"]).size().reset_index(name="CantidadPedidos")
    plt.figure(figsize=(12, 6))
    for año in dfgraf1['AñoPedido'].unique():
        datos_por_año = dfgraf1[dfgraf1['AñoPedido'] == año]
        plt.plot(datos_por_año['MesPedido'], datos_por_año['CantidadPedidos'], marker='o', label=f'Año {año}')
    plt.title('Evolución Mensual de Pedidos por Año')
    plt.xlabel('Mes')
    plt.ylabel('Cantidad de Pedidos')
    plt.xticks(range(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()
    ######Muestra grafico de torta de la cantidades de pedidos segun prioridad
    dfgraf2 = df.groupby(["Prioridad"]).size().reset_index(name="CantidadPrioridad")
    plt.rcParams["figure.figsize"] = 9,5
    def mostrar_cantidad(pct):
        total = sum(dfgraf2["CantidadPrioridad"])
        cantidad = int(round(pct * total / 100.0))
        return f'{cantidad}\n({pct:.1f}%)'
    plt.pie(dfgraf2["CantidadPrioridad"], labels=dfgraf2["Prioridad"], autopct=mostrar_cantidad)
    plt.title('Cantidad de Pedidos segun Prioridad')
    plt.show()

df = leer_excel("ventas")
#series()
#dataframes()
#df = filtrado_seleccion(df)
#df = faltantes(df)
#df = operaciones(df)
#df = transformacion(df)
df = combinaciones(df)
MostrarDatos(df)
#MostrarGrafico(df)
