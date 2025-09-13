#Ejercicios (Recorridos)

#Pedir una palabra y contar cuántas vocales tiene.
#Ingresar 4 palabras y mostrar únicamente las que contengan la letra 'r'.
#Ingresar palabras hasta escribir FIN; imprimir las que empiecen y terminen con la misma letra.


palabra = input("ingrese una palabra: ")

# contar vocales
palabra.lower()
cantVocales = 0

for ch in palabra:
    if ch == "a":
        cantVocales += 1
    if ch == "e":
        cantVocales += 1
    if ch == "i":
        cantVocales += 1
    if ch == "o":
        cantVocales += 1
    if ch == "u":
        cantVocales += 1
        
print("La palabra contiene:",cantVocales,"vocales")

listaPalabras = [input("ingrase la palabra 1: "),input("ingrese la palabra 2: "),input("ingrese la palabra 3: "),input("ingrese la palabra 4: ")]

for i in listaPalabras:
    contieneR = False
    for ch in i:
        if ch == "r":
            contieneR = True
    if contieneR:
        print("La palabra",i,"contiene R")
        
    