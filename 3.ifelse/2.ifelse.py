
# *************************************
# **** Python if – Sentencia básica ***
# *************************************

"""

En Python, la sentencia if se utiliza para ejecutar un bloque de código si,
y solo si, se cumple una determinada condición. 
Por tanto, if es usado para la toma de decisiones.

La estructura básica de esta sentencia if es la siguiente:

if condición:
    bloque de código

"""

"""

a = 5
b = 5

if (a == b):
    print("inguales")
else:
    print("no son iguales")

if (a > 100):
    print("mayor")
else:
    print("menor")
x = 10



if x < 20:
    print('x es menor que 20')

if x % 2 == 0:
    print('x es par')

if x != 5:
    print('x diferente')
"""


# *************************************
# **** Sentencia if … else  ***********
# *************************************

"""
Hay ocasiones en que la sentencia if básica no es suficiente
y es necesario ejecutar un conjunto de instrucciones o sentencias
cuando la condición se evalúa a False.

Para ello se utiliza la estructura if ... else... Esta es estructura es como sigue:

if condición:
    bloque de código (cuando condición se evalúa a True)
else:
    bloque de código 2 (cuando condición se evalúa a False)

"""
"""
x = 20
if x <= 10:
    print("x es menor")
else:
    print("x es mayor")

"""
"""

x = 2
n1 = int(input("n1: "))
n2 = int(input("n1: "))

if x == 1:
    print(n1+n2)
else:
    print(n1*n2)

"""

# *************************************
# **** Sentencias if anidadas  ***********
# *************************************

"""
x = int(input("numero: "))
if x >= 10:
    if x >= 10 and x < 20:
        print(f'{x} esta dentro del rango 10 - 19 ')
    else:
        print(f'{x} es mayor que el rango 10 - 19')

else:
    if x >= 1 and x <= 5:
        print(f'{x} esta dentro del rango 1 - 5')
    else:
        print(f'{x} es mayor que el rango 1 - 5')
"""

# *************************************
# **** if … elif … else  ***********
# *************************************

"""
También es posible que te encuentres situaciones en que una decisión dependa
de más de una condición.

En estos casos se usa una sentencia if compuesta, cuya estructura es como 
se indica a continuación:

if cond1:
    bloque cond1 (sentencias si se evalúa la cond1 a True)
elif cond2:
    bloque cond2 (sentencias si cond1 es False pero cond2 es True)
else:
    bloque else (sentencias si todas las condiciones se evalúan a False)

"""
"""
print("*******************************")
print("1.suma")
print("2.resta")
print("3.multiplicacion")
print("4.division")


opcion = int(input("opcion: "))
n1 = int(input("n1: "))
n2 = int(input("n1: "))

if opcion == 1:
    print(n1+n2)

elif opcion == 2:
    print(n1-n2)

elif opcion == 3:
    print(n1*n2)

elif opcion == 4:
    print(n1/n2)

else:
    print("nada")
"""
