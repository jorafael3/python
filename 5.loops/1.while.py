# *************************************
# **** while en Python           ******
# *************************************

"""
En ocasiones, tenemos que repetir varias veces una determinada tarea 
hasta conseguir nuestro objetivo. En Python esto se realiza con el comando while. 

el uso principal de la sentencia while es ejecutar repetidamente un bloque de código mientras se cumpla una condición.

La estructura de esta sentencia while es la siguiente:

while condición:
    bloque de código


Es decir, mientras condición se evalúe a True, se ejecutarán las instrucciones 
y sentencias de bloque de código.

Aquí, condición puede ser un literal, el valor de una variable, 
el resultado de una expresión o el valor devuelto por una función.

"""

"""
numero =0
print('numeros del 1 al 10')
while numero <= 10:
    print(numero)
    numero += 1
    #numero = numero +1
print('Fin')

"""
"""
import os
clear = lambda: os.system('cls')

fin = 1
while fin == 1:
    clear()
    mensaje = ('1.Mostrar mensaje \n'
           '2.finalizar\n')
    opcion = int(input(mensaje+": "))

    if opcion == 1:
        print("continuar ")

    elif opcion ==2:
        print("finalizado ")
        fin = 2


"""

print('tabla del 2')
tabla = 2
numero = 0
while numero <= 10:
    cal = numero *  tabla
    print(cal)
    numero += 1
    #numero = numero +1
print('Fin')



