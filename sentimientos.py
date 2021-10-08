#Se importa la libreria SentimentIntensityAnalyzer de la biblioteca nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer 

#nltk es una libreria de procesamiento de lenguaje natural
#SentimentIntensityAnalyzer recibe un string y devuelve un diccionario de puntajes
#entre -1 y 1

a = "death"  #Textos asignados a variables para probar el analizador de sentimientos
b = "It is a horrible experience!!!"
c = "I love my girlfriend"
d = "The movie was too good"
e = "Hello my pretty girlfriend"
f = "Please, help me"
g = "No"
h = "Yes"
i = "You are so beatifull"
#Todos los anteriores textos se asignan en variables para probar el reconocimiento de emociones en textos

sid = SentimentIntensityAnalyzer() #Instancia de objeto, en este caso sid se le asigna el analizador de sentimientos
resultados = sid.polarity_scores(g) #Crea el objeto de clase y se llama el metodo polarity, se le asigna un valor entre -1 y 1, luego un ponderado

print(resultados) #Impresion de resultados segun el texto asignado en la variable