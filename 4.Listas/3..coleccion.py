
# *************************************
# **** Diccionarios en Python    ******
# *************************************

"""
En Python, podemos tener una lista o un array de diccionarios. 
En tal objeto, cada elemento de una lista es un diccionario. 
Se puede acceder a cada diccionario utilizando su índice.

"""
anio = "2022"
autos = []

kia ={"modelo1":"sportage","modelo2":"rio","anio":anio,"marca":"kia"}
chevrolet ={"modelo1":"corsa","modelo2":"captiva","anio":anio,"marca":"chevrolet"}

autos.append(kia)
autos.append(chevrolet)

print(autos[0])



