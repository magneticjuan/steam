# En este archivo encontraremos las funciones básicas durante el proceso de proyecto, funciones que se repiten en varias ocasiones para ahorrar lineas de código

import pandas as pd
import json
import unicodedata
import nltk  
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns
import pyarrow as pa
import pyarrow.parquet as pq

def cargar_datos_json(ruta_archivo, nombre_dataframe):
    """
    Carga datos tipo JSON en un DataFrame de pandas.

    Parámetros:
    ruta_archivo (str): La ruta del archivo JSON que se va a cargar.
    nombre_dataframe (str): El nombre que se desea dar al DataFrame resultante.

    Retorna:
    pd.DataFrame: Un DataFrame de pandas con los datos cargados desde el archivo JSON.
    """
    fila = [] # lista vacia para ir guardando las filas
    with open(ruta_archivo) as ruta: # utilizo with para que el archivo se abra y cierre
        for linea in ruta.readlines(): # bucle para ir leyendo filas y luego agregarlas a row
            data = json.loads(linea)
            fila.append(data)

    # genero el dataframe y le asigno el nombre especificado
    dataframe_resultado = pd.DataFrame(fila)
    dataframe_resultado.name = nombre_dataframe
    return dataframe_resultado

def porcentaje_datos_vacios(df):
    """
    Calcula y muestra el porcentaje de datos vacíos por columna en un DataFrame.

    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.
    """
    total_filas = len(df)
    print("Porcentaje de datos vacíos por columna en el DataFrame:")
    for columna in df.columns:
        datos_vacios = df[columna].isnull().sum()
        porcentaje_vacios = (datos_vacios / total_filas) * 100
        print(f"{columna}: {porcentaje_vacios:.2f}%")
    print(f"Total de datos vacíos en el DataFrame: {(df.isnull().sum().sum() / (total_filas * len(df.columns))) * 100:.2f}%")

def limpiar_generos(generos):
    """
    Limpia los géneros de un juego.

    Parameters:
        generos (str or list): Los géneros del juego.

    Returns:
        str: El primer género limpio del juego.
    """
    if isinstance(generos, list):
        return generos[0]
    elif isinstance(generos, str):
        return generos
    else:
        return 'Pending'

def normalizar_texto(texto):
    """
    Normaliza el texto (convierte a mayúsculas y elimina acentos).

    Parameters:
        texto (str): El texto a normalizar.

    Returns:
        str: El texto normalizado.
    """
    if isinstance(texto, str):
        texto = texto.upper()
        texto = ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')
    return texto

def rellenar_nulos(row, precios_por_categoria_y_fecha):
    """
    Rellena los valores nulos en la columna "price" con la media correspondiente.

    Parameters:
        row (pandas.Series): La fila actual del DataFrame.
        precios_por_categoria_y_fecha (pandas.DataFrame): DataFrame con precios por categoría y fecha.

    Returns:
        float: El valor rellenado para la fila actual.
    """
    if pd.isnull(row['price']):
        categoria = row['genres']
        fecha = row['year']
        if (categoria, fecha) in precios_por_categoria_y_fecha.index:
            return precios_por_categoria_y_fecha[categoria, fecha]
    return row['price']

def analizar_sentimiento(reseña):
    """
    Analiza el sentimiento de una reseña utilizando la biblioteca SentimentIntensityAnalyzer de NLTK.

    Parameters:
        reseña (str): La reseña a analizar.

    Returns:
        int: Un valor numérico que representa el sentimiento de la reseña.
        - 2 si el sentimiento es positivo.
        - 1 si el sentimiento es neutral.
        - 0 si el sentimiento es negativo.

        Si la reseña es None, se devuelve 1 por defecto.
    """
    if reseña is None:
        return 1

    analizador = SentimentIntensityAnalyzer()
    puntaje_sentimiento = analizador.polarity_scores(reseña)['compound']

    if puntaje_sentimiento > 0.4:
        return 2
    elif puntaje_sentimiento < -0.5:
        return 0
    else:
        return 1

def cargar_datos_parquet(ruta_archivo):
    try:
        # Cargar el archivo Parquet en un DataFrame de Pandas
        dataframe_parquet = pd.read_parquet(ruta_archivo)
        return dataframe_parquet
    except Exception as e:
        print("Error al cargar los datos Parquet:", e)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualizar_distribucion(datos, columna, titulo, xlabel, ylabel):
    """
    Visualiza el top 10 de la distribución de datos en una columna específica.

    Parameters:
        datos (pandas.DataFrame): Los datos que se desean visualizar.
        columna (str): El nombre de la columna que se desea visualizar.
        titulo (str): El título del gráfico.
        xlabel (str): La etiqueta del eje x.
        ylabel (str): La etiqueta del eje y.
    """
    # Contar la frecuencia de los valores en la columna
    conteo = datos[columna].value_counts().head(10)
    
    plt.figure(figsize=(10, 8))
    ax = sns.barplot(x=conteo.values, y=conteo.index, palette='colorblind')
    ax.set_title(titulo, fontsize=16)
    ax.set_xlabel(xlabel, fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)
    plt.show()

def visualizar_distribucion_circular(datos, columna, titulo):
    """
    Visualiza la distribución de datos en una columna específica en un gráfico circular.

    Parameters:
        datos (pandas.DataFrame): Los datos que se desean visualizar.
        columna (str): El nombre de la columna que se desea visualizar.
        titulo (str): El título del gráfico.
    """
    # Contar la frecuencia de los valores en la columna
    conteo = datos[columna].value_counts()

    # Mapear los valores a sus correspondientes categorías
    categorias = {0: 'Negativo', 1: 'Neutral', 2: 'Positivo'}
    labels = [categorias.get(valor, valor) for valor in conteo.index]
    
    # Crear un gráfico circular
    plt.figure(figsize=(8, 8))
    plt.pie(conteo, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(titulo)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Agregar leyenda
    plt.legend(labels=labels)
    
    plt.show()

def guardar_datos(datos, ruta):
    """
    Guarda datos en un archivo en formato Parquet.

    Parameters:
        datos (pandas.DataFrame): Los datos que se desean guardar.
        ruta (str): La ruta donde se desea guardar el archivo Parquet.
    """
    tabla = pa.Table.from_pandas(datos)
    pq.write_table(tabla, ruta)