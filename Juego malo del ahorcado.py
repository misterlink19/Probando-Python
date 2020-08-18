# Juego malo del ahoracado
# Se llama asi porque el profe cuando nos enseñó
# el codigo sencillo dijo que era un juego malo, y
# pues le puse ese nombre.
# Ahora el juego fue mejorado, muestra dibujo del estado
# del hombre cuando no aciertas a la palabra.
# Pueden mejorar el juego y agregarle cosas, para que sea mas chevere

# Random para usar la funcion de elegir al azar una palabra de una lista
# Ahorcado es un archivo py, que tiene el codigo de dibujar todo en pantalla
import random
from Ahorcado import ahorcado_dibujo, titulo_del_ahorcado

archivo = open("Palabras.txt","r")
palabras = archivo.read().splitlines()
archivo.close()

palabra = str(random.choice(palabras))
letras = list(palabra)
random.shuffle(letras)

titulo_del_ahorcado()

# Esto chequea que la palabra no aparezca igual
# luego de ponerlas al azar.
while "".join(letras) == palabra:
    random.shuffle(letras)


print("Pista:",",".join(letras))
intentos = 7
ahorcado_dibujo(intentos)

# Este es el codigo principal, el que revisa
# si el usuario acertó o no.
while intentos:
    print(f"Numero de intentos: {intentos}")
    
    respuesta = input ("Entra tu repuesta: ")
    
    if respuesta.lower() == palabra.lower():
        ahorcado_dibujo(10)
        break

    intentos -=1    
    print("\nFallaste...")

    if intentos > 0:
        ahorcado_dibujo(intentos)
        print("Pista:",",".join(letras))
else:
    ahorcado_dibujo(intentos)
