#Ejercicios (Funciones)

#Escribir es_palindromo(cadena) que devuelva True si la cadena se lee igual al derecho y al revés (ignorar espacios y mayúsculas/minúsculas).
#Escribir contar_vocales(cadena) que retorne un diccionario con la cuenta de cada vocal.
#Escribir normalizar_palabras(frase) que retorne una lista de palabras sin signos de puntuación y en minúsculas.

palabra = input("Escribir una palabra: ")

def palindormo():
    for i, j in range (len(palabra)):
        i + 1
        j - 1
        
        if palabra[i] == palabra [j]:
            return True
    
