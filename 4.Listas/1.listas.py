# *************************************
# **** Listas en Python          ******
# *************************************

"""

Son listados de datos en los que hay un orden, 
por lo que tiene en cuenta la posición en la que está el elemento. 
Recuerda que el primer elemento es el número 0, y no el número 1. 
En las listas se pueden modificar sus elementos, y puede haber elementos duplicados. 
Se crean poniendo sus elementos entre corchetes

"""

autos=["ferrari", "chevrolet","suzuki"]
#print(autos)


#Acceder a un elemento de la lista.
#print(autos[1])

# append: Añadimos al final de la lista
autos.append("lada")
#print(autos)

# pop: Extraemos con el indice o posicion del elemento
autos.pop(0)
#print(autos)

# insert: Añadimos al inicio
autos.insert(0,"porshe")
#print(autos)


 # extend: Juntamos
autos2 = ["Gmc","mazda"]
autos.extend(autos2)
#print(autos)

#remove: Borramos con el valor

autos.remove("chevrolet")
#print(autos)
