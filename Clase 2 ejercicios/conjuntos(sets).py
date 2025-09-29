#Pedir dos listas de números (separados por espacios) y mostrar su intersección usando set.
#Eliminar duplicados de una lista manteniendo el orden (pista: usar un set auxiliar para vistos).

listaUsuario1 = []
listaUsuario2 = []

while True:
    ingreso = int(input("ingrese un numero para la primera lista: "))
    print("para terminar ingrese -1")
    if ingreso == -1:
        break
    else:
        listaUsuario1.append(ingreso)
        
while True:
    ingreso = int(input("ingrese un numero para la segunda lista: "))
    print("para terminar ingrese -1")
    if ingreso == -1:
        break
    else:
        listaUsuario2.append(ingreso)
        
setLista1 = set(listaUsuario1)
setLista2 = set(listaUsuario2)

print("interseccion de las listas: ", setLista1 & setLista2)

##########----------------------##############

listaDuplicados = [1,1,2,3,3,3,4,2,5,1]

vistos = set()
listaSinDuplicados = []

for x in listaDuplicados:
    if x not in vistos:
        listaSinDuplicados.append(x)
        vistos.add(x)

print("lista sin duplicados: ", listaSinDuplicados)
