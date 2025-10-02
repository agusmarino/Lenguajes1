lista = [1,2,3,4,5,6,7,8]

from utlidades import promedio
from utlidades import suma

promedio(lista)

print("----------------")

suma(lista)
print("--------------------")

import math

def raizCua(lista):
    raices = []
    for i in lista:
        raiz = math.sqrt(i)
        raices.append(raiz)
    print(raices)
    
raizCua(lista)
print("---------------")

def natLog(lista):
    logs = []
    for i in lista:
        loga = math.log(i)
        logs.append(loga)
    print(logs)
    
natLog(lista)

contador = 0 

def aumentar():
    contador += 1
    print(contador) #
    
#aumentar() no funciona porque python asume que es una variable local

def variable ():
    x = 100
    print(x)
    
variable()
x = 100
print(x)

#pyhton una la variable global


#ej 6
import builtins

printOG = builtins.print

def printSobre(*args, **kwargs):
    printOG("---",*args,"----")
    
builtins.print = printSobre

print("hola")

builtins.print = printOG

print("hola")


#ej 7
def suma_total(*args):
    suma = 0
    for i in args:
        suma = suma + i
    print(suma)
    
suma_total(1,2,3,4,54)

#ej 8

def mostrar_info(**kwargs):
    print(kwargs)
        
mostrar_info(nombre= "agus", localidad = "la plata")

#ej 9

def mostrar(*args,**kwargs):
    puntos = 0
    for i in args:
        puntos += puntos + i
        
    print(puntos)
    print(kwargs)
    
mostrar(1,2,3,4,54, nombre= "agus", localidad = "la plata")

