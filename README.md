## Proyecto Final: API de Consultas sobre Juegos de la Plataforma Steam

En este proyecto, se ha desarrollado una API para realizar consultas sobre juegos de la plataforma Steam. La API permite a los usuarios obtener información detallada sobre desarrolladores, usuarios, géneros, reseñas y recomendaciones de juegos.

### Archivos del Proyecto

### Archivo `main.py`

Este archivo contiene el código principal de la API desarrollada en Python utilizando el framework FastAPI. Aquí se definen las rutas y funciones para manejar las solicitudes HTTP GET de los usuarios. Las funciones implementadas en este archivo permiten obtener información detallada sobre desarrolladores, usuarios, géneros, reseñas y recomendaciones de juegos de la plataforma Steam.

Los datos utilizados por la API se cargan desde archivos Parquet preprocesados, los cuales se generaron a partir de datos originales en formato JSON. Estos archivos Parquet proporcionan acceso rápido a los datos y permiten consultas eficientes en la API.

La API se ha desplegado y está disponible en el siguiente enlace: [API de Consultas sobre Juegos de Steam](https://repo-api-doo4.onrender.com)

### Archivo `funciones_basicas.py`

En este archivo se encuentran funciones básicas que son utilizadas en todo el proyecto para cargar datos, limpiar datos y realizar operaciones comunes. Estas funciones incluyen la carga de datos desde archivos JSON, la normalización de texto, el análisis de sentimientos y la manipulación de datos faltantes, entre otras.

Los datos originales se obtuvieron en formato JSON y luego se procesaron y transformaron utilizando estas funciones básicas antes de ser almacenados en archivos Parquet para su uso en la API.

### Archivo `Modelado.ipynb`

Este archivo es un cuaderno Jupyter que contiene el proceso de modelado y creación de un modelo de recomendación de juegos similares utilizando similitud coseno. En este cuaderno se carga el conjunto de datos, se realiza la preprocesamiento de los datos, se entrena el modelo y se evalúa su rendimiento.

El modelo de recomendación se utiliza en la API para proporcionar a los usuarios una lista de juegos similares a uno dado como entrada.

### Directorio `PARQUET`

Este directorio contiene archivos Parquet que almacenan datos preprocesados y transformados para su uso en la API. Los archivos Parquet se generaron a partir de los datos originales en formato JSON utilizando las funciones definidas en `funciones_basicas.py`. Los archivos Parquet proporcionan un acceso rápido y eficiente a los datos y se utilizan en la API para realizar consultas y devolver respuestas rápidas a los usuarios.

### Proceso de Desarrollo

El proyecto siguió un proceso de desarrollo iterativo que incluyó la adquisición de datos desde archivos JSON, el preprocesamiento y transformación de los datos utilizando funciones básicas, el desarrollo de la API utilizando FastAPI, pruebas exhaustivas y depuración de errores, y la documentación del proyecto en un archivo README.md.

La API desarrollada proporciona a los usuarios una forma fácil y eficiente de acceder a información detallada sobre juegos de la plataforma Steam, así como recomendaciones personalizadas basadas en sus preferencias.

### Descripción de Funciones

A continuación, se presenta una descripción detallada de las funciones principales definidas en `main.py` y en `funciones_basicas.py`:

Claro, a continuación, explicaré en detalle cada una de las funciones mencionadas anteriormente, indicando en qué archivo se encuentra y para qué sirve cada una:

### Archivo `main.py`

1. **inicio**: Esta función maneja la solicitud GET a la ruta raíz ("/") de la API y devuelve una página HTML de bienvenida que describe la funcionalidad de la API.

2. **developer**: Esta función maneja la solicitud GET a la ruta "/developer/{desarrollador}" y devuelve información sobre la cantidad y porcentaje de juegos gratuitos por año para un desarrollador específico.

3. **userdata**: Esta función maneja la solicitud GET a la ruta "/userdata/{usuario}" y devuelve información sobre un usuario específico, incluyendo la cantidad de dinero gastado, el porcentaje de recomendación y la cantidad de items.

4. **UserForGenre**: Esta función maneja la solicitud GET a la ruta "/userforgenre/{genero}" y devuelve información sobre el usuario con más horas jugadas para un género dado, así como una lista de la acumulación de horas jugadas por año de lanzamiento.

5. **best_developer_year**: Esta función maneja la solicitud GET a la ruta "/bestdeveloperyear/{year}" y devuelve el top 3 de desarrolladores con los juegos más recomendados por usuarios para un año dado.

6. **DeveloperReviewsAnalysis**: Esta función maneja la solicitud GET a la ruta "/developerreviewsanalysis/{desarrolladora}" y devuelve información sobre la cantidad total de registros de reseñas de usuarios categorizados con un análisis de sentimiento como positivo o negativo para un desarrollador específico.

7. **recomendacion_juego**: Esta función maneja la solicitud GET a la ruta "/recomendacion_juego/{id}" y devuelve una lista de 5 juegos similares a un juego dado (identificado por su ID).

### Archivo `funciones_basicas.py`

1. **cargar_datos_json**: Esta función se encuentra en el archivo `funciones_basicas.py` y se utiliza para cargar datos tipo JSON en un DataFrame de pandas.

2. **porcentaje_datos_vacios**: Esta función calcula y muestra el porcentaje de datos vacíos por columna en un DataFrame.

3. **limpiar_generos**: Esta función limpia los géneros de un juego, devolviendo el primer género limpio.

4. **normalizar_texto**: Esta función normaliza el texto, convirtiéndolo a mayúsculas y eliminando acentos.

5. **rellenar_nulos**: Esta función rellena los valores nulos en la columna "price" con la media correspondiente.

6. **analizar_sentimiento**: Esta función analiza el sentimiento de una reseña utilizando la biblioteca SentimentIntensityAnalyzer de NLTK.

7. **cargar_datos_parquet**: Esta función carga datos desde un archivo en formato Parquet y devuelve un DataFrame de pandas.

8. **visualizar_distribucion**: Esta función visualiza el top 10 de la distribución de datos en una columna específica.

9. **visualizar_distribucion_circular**: Esta función visualiza la distribución de datos en una columna específica en un gráfico circular.

10. **guardar_datos**: Esta función guarda datos en un archivo en formato Parquet.

### Proceso de Desarrollo

El proyecto ha seguido un proceso de desarrollo iterativo, que incluye las siguientes etapas:

1. **Adquisición de Datos**: Se usaron los datasets en formato tipo JSON.

2. **Preprocesamiento de Datos**: Los datos recopilados se limpiaron, transformaron y se almacenaron en archivos Parquet para un acceso rápido y eficiente.

3. **Desarrollo de la API**: Se implementó una API utilizando el framework FastAPI en Python. Se definieron las rutas y las funciones para manejar las solicitudes de los usuarios.

4. **Pruebas y Depuración**: Se realizaron pruebas exhaustivas para asegurar el correcto funcionamiento de la API. Se depuraron errores y se realizaron ajustes según sea necesario.

5. **Documentación**: Se creó un archivo README.md para proporcionar una guía detallada sobre el proyecto, incluyendo una descripción de los archivos, funciones y procesos involucrados.

El proyecto está diseñado para proporcionar a los usuarios una forma fácil y eficiente de acceder a información relevante sobre juegos de la plataforma Steam, así como recomendaciones personalizadas basadas en sus preferencias.
