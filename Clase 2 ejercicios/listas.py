# Ejercicios (Listas)

#Ingresar notas hasta -1, calcular el promedio y cuántos están por debajo.
#Dada una lista de palabras, construir otra con las que tengan más de 5 letras.

notas = [4, 6, 7, 3, 8, 10]
total = 0
menosPromedio = 0

for i in notas:
    total = total + i

promedio = total / len(notas)

for j in notas:
    if j < promedio:
        menosPromedio += 1

print("------------")
print("notas: ", notas)
print("nota promedio: ", promedio)
print("cantidad de notas menores al promedio: ",menosPromedio)

print("-----------")

palabras5 = ["cosas", "botella", "mate", "computadora", "monitor", "casa"]
palabrasMas= []

for i in palabras5:
    if len(i) > 5:
        palabrasMas.append(i)
        
print("lista de palabras: ", palabras5)
print("lista de las palabras con mas de 5 letras: ",palabrasMas)