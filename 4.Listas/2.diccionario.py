

# *************************************
# **** Diccionarios en Python    ******
# *************************************

"""

un diccionario en Python es una palabra que tiene asociado algo. 
Al contrario de lo que sucedía en las listas, los diccionarios no tienen orden.

Se crean poniendo sus elementos entre llaves {a:quito, b:guayaquil}. 
Se denominan keys a las «palabras» y values a las «definiciones».  
Lógicamente, no puede haber dos keys iguales, aunque sí dos values iguales.

"""
anio = "2022"
chevrolet ={"modelo1":"corsa","modelo2":"captiva","anio":anio}
#print(chevrolet)

# get(): Devuelve el valor que corresponde con la key introducida.
# tambien se puede acceder de la sgte manera dict[key]
marca1 = chevrolet.get("modelo1")
marca2 = chevrolet["modelo1"]

#print(marca1)

# pop(): Devuelve el valor que corresponde con la key introducida
#print(chevrolet.pop('modelo1'))
#print(chevrolet)

# update(): Actualiza el valor de una determinada key o lo crea si no existe.
chevrolet.update({"modelo2":"aveo"})
#print(chevrolet)

# "key" in diccionario: devuelve verdadero (True) o falso (False) 
# si la key existe en el diccionario.

#print("modelo1" in chevrolet)

# "definición" in diccionario.values(): devuelve verdadero (True) o falso (False) 
# si la definición  existe en el diccionario.

#print("aveo" in chevrolet.values())


# del diccionario['key']: Elimina el valor (y el key) asociado a la key indicada.
del chevrolet["modelo1"]

#print(chevrolet)