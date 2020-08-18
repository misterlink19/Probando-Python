import pyttsx3

#Oh un comentario de twitter xDD

#Texto a Voz
t4v = pyttsx3.init()

#Poniendolo en español
voices = t4v.getProperty('voices')
t4v.setProperty("voice",voices[-1].id)

saludo = """ 

Hola mundo

"""

t4v.say(saludo)
t4v.runAndWait()