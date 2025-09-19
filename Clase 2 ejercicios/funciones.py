#Ejercicios (Funciones)

#Escribir es_palindromo(cadena) que devuelva True si la cadena se lee igual al derecho y al revés (ignorar espacios y mayúsculas/minúsculas).
#Escribir contar_vocales(cadena) que retorne un diccionario con la cuenta de cada vocal.
#Escribir normalizar_palabras(frase) que retorne una lista de palabras sin signos de puntuación y en minúsculas.

import string

def contar_vocales(cadena):
    cadena = cadena.lower()
    vocales = "aeiou"
    conteo = {v: 0 for v in vocales}  # inicializa diccionario con 0
    
    for letra in cadena:
        if letra in conteo:
            conteo[letra] += 1
    return conteo

def normalizar_palabras(frase):
    # pasar a minúsculas
    frase = frase.lower()
    # quitar signos de puntuación
    for signo in string.punctuation:
        frase = frase.replace(signo, "")
    # dividir en palabras
    return frase.split()

def normalizar_palabras(frase):
    # pasar a minúsculas
    frase = frase.lower()
    # quitar signos de puntuación
    for signo in string.punctuation:
        frase = frase.replace(signo, "")
    # dividir en palabras
    return frase.split()
