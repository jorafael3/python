#************************************
#**************************
#****    VARIABLES   ******
#**************************
"""
Una variable es un sitio donde guardamos una determinada información.
En función del tipo de información que guardemos (texto, números, booleanas, 
retorno de funciones.),
la variable será de uno u otro tipo. 

Cada variable tiene que tener un nombre con el que referirnos a ella. 
Python tiene en cuenta si escribimos en mayúsculas o minúsculas la variable


En la operación de asignación se ven involucradas tres partes:

1.El operador de asignación =
2.Un identificador o nombre de variable, a la izquierda del operador
3.Un literal, una expresión, una llamada a una función o una combinación de 
    todos ellos a la derecha del operador de asignación

"""





a = 1
a = True
a = False
a = None
a = "hola"


#**************************
#**** TIPOS DE DATOS ******
#**************************

#**** NUMERICOS

"""

En números hay dos tipos principales, 
los números enteros (llamados int) y los reales (llamados float).
El separador decimal que tenemos que usar es el punto.
#variables numericas enteros
#variables numericas flotantes
#variables numericas long
#variables numericas complex

Aunque si no decimos el tipo de número que va a contener,
Python intentará decidir por si mismo cuál es el más apropiado,

"""

entero = 5
flotante = 2.5

entero = int(5)
flotante = float(2.5)

#**** TEXTO

"""
Las variables que almacenan texto se denominan strings (str).
Tienen que estar entre comillas sencillas(' ') o dobles (" "),
o si el texto ocupa varias líneas, entre triples comillas dobles ("""  """) .

"""

texto1='Esto es otro texto'
texto2="Esto es un texto"
texto3="""
Hola
caracola
"""
texto4 = str(4) 


#**** EJEMPLOS *******


hola = "hola"
print(hola)