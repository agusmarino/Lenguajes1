###Ejercicios (Strings)

#Pedir una palabra y mostrarla en mayúsculas, minúsculas y title case.
#Pedir una frase y contar cuántas veces aparece cada vocal.
#Dada una frase, mostrar las 3 primeras y las 3 últimas letras usando slicing.
#Verificar si una palabra contiene la letra 'r'. (Tip: in)

import string

palabra = input("Ingrese una palabra: ")
print("Mayúsculas:", palabra.upper())
print("Minúsculas:", palabra.lower())
print("Title Case:", palabra.title())
palabra.lower()
if 'r' in palabra:
    print("la palabra contiene la letra r")
else:
    print("la palabra no contiene la letra r")

frase = input("Ingrese una frase: ")
cantVocales = 0

frase.lower()

for ch in frase:
    if ch == 'a':
        cantVocales += 1
    if ch == 'e':
        cantVocales += 1
    if ch == 'i':
        cantVocales += 1
    if ch == 'o':
        cantVocales += 1
    if ch == 'u':
        cantVocales += 1
        
print("cantidad de vocales en la frase: ", cantVocales) 

print("primeras 3 letras de la frase: ")
print(frase[:3]) #primeras 3 letras
print("Ultimas 3 letras de la frase: ")
print(frase[-3:]) #ultimas 3 letras

