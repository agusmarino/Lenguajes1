# Ejercicios (Tuplas)

#Guardar coordenadas (x, y) en una tupla e imprimir la distancia al origen.
#Dada una lista de tuplas (nombre, edad), imprimir solo los mayores de 18.

coordenadas = (int(input("ingrese el punto x: ")), int(input("ingrese el punto y: ")))
x,y = coordenadas

distanciaOrigen = (x ** 2 + y ** 2)** 0.5

print("La distacia al origen de el punto x,y es: ", distanciaOrigen)

print("----------")

#----------------

lista = []
print("para terminar de ingresar escribir nombre: 0 y edad: 0")

while True:
    tupla = (input("ingresar nombre: "),int(input("Ingresar edad: ")))
    if tupla == ("0",0):
        break
    lista.append(tupla)

print("personas ingresadas mayores de 18 años: ")

for i in lista:
    if i[1] >= 18:
        print(i)
        
 