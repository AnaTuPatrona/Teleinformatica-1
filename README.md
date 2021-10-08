# Teleinformática 1

### Integrantes
- Fabian Alexander Franco Quiroga – 20152020048
- Sebastián Mora Arguelles - 20141020117

## Analizador de emociones en textos
Analizador de emociones en textos por medio de Python que nos permita leer un archivo CSV y determinar el porcentaje de negatividad, neutralidad y positividad.

<p align="center">
  <img width="500" src="http://akashsenta.com/blog/wp-content/uploads/2019/07/Sentiment_analysis_with_vader_akashsenta.com_.jpg">
</p>

## Lenguaje
El proyecto se desarrollo completamente en la herramienta **Python** junto con la ayuda de diferentes bibliotecas para el analisis de sentimientos en textos y para la interpretación, manejo y correcto uso de los datasets utilizados en este proyecto.

<p align="center">
  <img width="500" src="https://www.icog.es/cursos/wp-content/uploads/2020/09/phyton.png">
</p>

## Requerimientos 
Para la realización de este proyecto necesitaremos tener instalado el lenguaje de **Python** y dentro de este tener las siguientes librerias de **Python** para trabajar nuestro proyecto:

- Numpy+MKL
- Marisa-trie
- Pandas
- Spanish_sentiment_analysis
- ipython
- NLTK - Vader

<p align="center">
  <img width="500" src="https://thinktecno.com/wp-content/uploads/2020/11/1605037028_Como-instalar-un-modulo-de-Python-con-PIP.png">
</p>

Para la instalación de estas librerias, se tiene que abrir la consola de **Python** ya sea desde el IDLE o algun otro programa que permita trabajar este lenguaje y luego escribir el comando ***pip install*** acompañado de la libreria que se va a instalar. A continuacion se mostrara unos ejemplos de como se instalarian librerias: 
 
 - *pip install numpy*
 - *pip install pandas*
 - *pip install ipython*

Si se desea conocer mas sobre la instalación de librerias de **Python** seleccione el siguiente enlace de [documentación.](https://programminghistorian.org/es/lecciones/instalar-modulos-python-pip)

## Ejecución, desarrollo e implementación de la aplicación

Para ejecutar este aplicativo deberemos tener el IDLE de **Python** o algun otro editor de codigo, para este caso se recomienda usar [Visual Studio Code](https://code.visualstudio.com/), ya que nos ayudara en la organización y visualización de archivos, para la correcta ejecución de la aplicación. 

<p align="center">
  <img width="500" src="https://sobrebits.com/wp-content/uploads/2018/10/Visual-Studio-Code-para-PowerShell.png">
</p>

Se recomienda seguir el orden de ejecución presentado a continuación:

1. Instalación de librerias

    Teniendo abierto nuestro *Visual Studio Code*, nos dirigimos a la consola del editor e instalamos las librerias mencionadas anteriormente en la descripción de este proyecto, con el comando *pip install.*

    **Librerias**

    - Numpy+MKL
    - Marisa-trie
    - Pandas
    - Spanish_sentiment_analysis
    - ipython
    - NLTK - Vader

2. Replica del codigo

    Luego de la instalación de librerias, pasaremos a la replica de este codigo, se tienen que descargar los archivos de este repositorio dentro de una carpeta de trabajo. Luego damos clic derecho sobre la carpeta y le damos a **abrir con code***, esto nos abrira nuestro proyecto en nuestro editor, logrando ver los archivos del codigo y los dos datasets necesarios para probar y ejecutar el aplicativo. 
    
3. Ejecución de aplicativo

    Para ejecutar simplemente nos ubicamos en el archivo que queramos ejecutar, puede ser el archivo ***"sentimientos"*** que nos permite analizar frases o palabras contenidas en variables o el archivo ***"sentimientos_ingles"*** que nos permite analizar un gran dataset de datos. Incluimos 2 datasets para probar y ejecutar el programa, uno es pequeño para comprobar mas facil los resultados y uno mas extenso para probar el alcance de nuestro aplicativo. 
    
    <p align="center">
      <img width="200" src="https://miro.medium.com/max/1184/0*zKRz1UgqpOZ4bvuA">
    </p>
    
## Documentación de apoyo

Para apoyo en cuanto a la instalación o documentación de lo utilizado en este aplicativo, se adjuntan los siguientes enlaces direccionando a información de apoyo:

- [Análisis de sentimiento - NLTK](https://www.nltk.org/_modules/nltk/sentiment/vader.html)
- [Sobre librerias de Python](https://pythones.net/importar-modulos-en-python/)
- [Documento base analizador de sentimientos en historias de texto](https://ieeexplore.ieee.org/document/9070506)
