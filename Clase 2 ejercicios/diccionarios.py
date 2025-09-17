#Ejercicios (Diccionarios)

#Leer nombres y notas hasta FIN y guardar en un diccionario. Luego mostrar:
#Promedio general, mejor estudiante, y los/as que están por debajo del promedio.
#Construir un diccionario {palabra: longitud} a partir de una frase.

notas = {}

print("para terminar de ingresar nombre = fin")

while True:
    nombre = input("Ingrese el nombre : ")
    
    if nombre == "fin":
        break
    
    edad = input("Ingrese la edad: ")
    notas[nombre] = edad
    
print(notas)

