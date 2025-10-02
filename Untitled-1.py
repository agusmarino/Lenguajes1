
#¿Cómo se define un conjunto (set) en Python y qué propiedad principal lo caracteriza?

conjunto = {1,2,3,4,5,6}

lista = [1,2,2,2,3,4,5,6]

set(lista)

#propiedades

#sin elementos repetidos
print(lista)
print(set(lista))

#mutable

conjunto.add(7)
print(conjunto)
conjunto.remove(3)
print(conjunto)

#no tiene indice

#print(conjunto[1])
    
print(lista[1])
    
#operaciones conjuntos

union = conjunto | set(lista)
print(union)

interseccion = conjunto & set(lista)
print(interseccion)

diferencia = conjunto - set(lista)
print(diferencia)
