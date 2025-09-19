#Ejercicios (Diccionarios)

#Leer nombres y notas hasta FIN y guardar en un diccionario. Luego mostrar:
#Promedio general, mejor estudiante, y los/as que están por debajo del promedio.
#Construir un diccionario {palabra: longitud} a partir de una frase.

notas = {
    "agus": 10,
    "nico": 8,
    "fran": 4,
    "juli": 0
}

print("para terminar de ingresar nombre = fin")

# while True:
#     nombre = input("Ingrese el nombre : ")
    
#     if nombre == "fin":
#         break
    
#     nota = int(input("Ingrese la nota: "))
#     notas[nombre] = nota
    
print(notas)

sumaNotas = 0
max = -1
estudianteMejor = "def"

n = notas.values()

for i in n:
    sumaNotas += i

promedio = sumaNotas / len(n)
print(promedio)

listaMenosPromedio = []

h = notas.items()

for i in h:
    if i[1] < promedio:
        listaMenosPromedio.append(i)
        
print("el promedio general es: ", promedio)
print("el mejor promedio es: ", estudianteMejor,"su nota es: ",max)
print("los alumnos con nota menor al promedio son: ",listaMenosPromedio)


#.....................................
#....................................-

frase = input("Ingrese una frase: ")
diccionarioFrase = {}

for i in frase.split():
    palabra = i
    longitud = len(palabra)
    diccionarioFrase[palabra] = longitud
    
print(diccionarioFrase)