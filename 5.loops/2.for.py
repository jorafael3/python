import os
clear = lambda: os.system('cls')
# *************************************
# **** while en Python           ******
# *************************************

"""

El bucle for se utiliza para recorrer los elementos de un objeto iterable 
(lista, tupla, conjunto, diccionario, …) y ejecutar un bloque de código. 
En cada paso de la iteración se tiene en cuenta a un único elemento del objeto iterable, 
sobre el cuál se pueden aplicar una serie de operaciones

"""
"""
for n in range(5):
    print(n+1)

nums = [4, 78, 9, 84]
nombres = ["jorge", "juan", "erika", "priscila"]

for n in nombres:
    print(n)

"""


"""

Qué es un iterable

Un iterable es un objeto que se puede iterar sobre él, es decir, 
que permite recorrer sus elementos uno a uno


valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}

for k in valores:
    print(valores.get(k))
    print(valores[k])
    print(k)

"""


autos = []
anio = "2022"
kia ={"modelo1":"sportage","modelo2":"rio","anio":anio,"marca":"kia"}
chevrolet ={"modelo1":"corsa","modelo2":"captiva","anio":anio,"marca":"chevrolet"}

autos.append(kia)
autos.append(chevrolet)

#print(autos)

for marcas in len(autos):
    print(marcas)



