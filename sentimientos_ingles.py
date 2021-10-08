#Se importa la libreria SentimentIntensityAnalyzer de la biblioteca nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#nltk es una libreria de procesamiento de lenguaje natural
#SentimentIntensityAnalyzer recibe un string y devuelve un diccionario de puntajes
#entre -1 y 1

import pandas as pd
#se importa la libreria pandas para nanipular facilmente el dataset
#La libreria pandas nos permitira el analisis de  grandes cantidades de datos, esto de un archivo CSV

sid = SentimentIntensityAnalyzer() 
#se asigna la funcion a la variable sid, esta funcion es la que se importa del nltk vader (Analizador de emociones)

df = pd.read_csv("dataset2.csv") #Variable lee archivos
#se lee el dataset .CSV con las frases a reconocer y se asigna a la varible df
#Esto se hace para el analisis de emociones en la frase

df["sentimiento"] = df["mensaje"].apply(lambda i: sid.polarity_scores(i)['compound']) #Polaridad del mensaje
#A la columna mensaje existente en el dataset se le aplica la funcion lambda
#Lamba utiliza el analizador de sentimientos para encontrar la polaridad de cada frase -1 a 1
#i es el parametro de la funcion que le asigna el score a cada frase

df.to_csv('clasificacionsentimientos.csv') #Se guarda el archivo analizado
#Se guarda el archivo con la trasnformación y los scores de cada una de las frases