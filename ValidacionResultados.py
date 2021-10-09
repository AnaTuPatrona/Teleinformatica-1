
#Se importa la libreria pandas 
import pandas as pd
#Se importa la libreria Numpy
import numpy as np
#Se asigna el nuevo dataset generado con los scores de la clasificacion a la variable df
df = pd.read_csv("mensajes_con_sentimientos.csv")

#con el dataframe cargado en df pasamos cada valor de la columna 
# sentimiento (score) a la columna isinstance y se verifica que todos 
# los scores sean valores numericos. Devuelve un arreglo booleano y
#devuelve las filas donde el resultado es verdadero
df[df['sentimiento'].apply(lambda x: isinstance(x, (int, np.int64)))]

#una vez verificado que los scores son numeros se declara la funcion
# Clasifica , la cual permite asignar una etiqueta a los puntajes
#para su clasificacion. Si el score es Mayor a 0 es positivo y si
#es menor que 0 es negativo
def Clasifica(s):
    if s > 0 :
        return 'Positivo'
    elif s <= 0 :
        return 'Negativo'
    return ''

#se llama a la funcion Clasifica que obtiene el parametro como cada valor
#de la columna sentimiento. Se crea una serie con el resultado que luego
#se asigna a la nueva columna Polaridad de acuerdo a la comparacion
df['Polaridad'] = df['sentimiento'].apply(Clasifica)

#se muestra el dataset con la nueva columna Polaridad
df

#por ultimo se obtienen los porcentajes de participacion de cada elemento
# a traves de la funcion value_counts que cuenta la cantidad de repeticiones
#de cada clasificacion y las divide por el total de registros
(df['Polaridad'].value_counts()/df['Polaridad'].count())*100
