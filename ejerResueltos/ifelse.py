"""
Ejercicio 1

Escribir un programa que pregunte al usuario su edad y muestre por pantalla 
si es mayor de edad o no.

"""

"""

Ejercicio 2

Escribir un programa que pida al usuario un número entero y 
muestre por pantalla si es par o impar.

"""


"""
Ejercicio 3

Los alumnos de un curso se han dividido en dos grupos A y B 
de acuerdo al sexo. 

El grupo A esta formado por las mujeres 
los hombres el grupo B.

Escribir un programa que pregunte al usuario su nombre y sexo, y 
muestre por pantalla el grupo que le corresponde.

"""



"""
Ejercicio 4

Realiza un programa que lea 2 números por teclado y determine
los siguientes aspectos e imprimir

Si los dos números son iguales
Si los dos números son diferentes
Si el primero es mayor que el segundo
Si el segundo es mayor o igual que el primero

n1 = int(input("n1: "))
n2 = int(input("n2: "))

if n1 == n2:
    print("son iguales")
elif n1 != n2:
    print("son diferentes")
elif n1 > n2:
    print(n1, "es mayor")
elif n1 < n2:
    print(n2, "es menor")
"""

"""

Ejercicio 5

Utilizando operadores lógicos, determina si una cadena de texto
introducida por el usuario tiene una longitud mayor o igual que 3 
y a su vez es menor que 10


texto = input("texto: ")
longitud = len(texto)
print("logitud: ",longitud)

if longitud >= 3 and longitud < 10:
    print("dentro del rango")
else:
    print("fuera del rango")

"""

"""
EJERCICIO 6

Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo 
o la de un círculo. 

Si se contesta que se quiere calcular el área de un triángulo 
(escribiendo T o t), el programa tiene que pedir entonces la base y la altura e 
imprimir el área. 

Si se contesta que se quiere calcular el área de un círculo 
(escribiendo C o c), el programa tiene que pedir entonces el radio e imprimir el área.


Se recuerda que el área de un triángulo es base por altura dividido por 2 
y que el área de un círculo es Pi (aproximadamente 3,141592) por el radio al cuadrado.

Nota: Utilice como valor de pi el valor 3.141592.

print("*********************************")
print("T. calcular area del triangulo")
print("C. calcular area del circulo")

opcion = input("escriba T o C: ")

if opcion == "T" or opcion == "t":
    base = int(input("base: "))
    altura = int(input("altura: "))
    res = (base * altura) / 2
    print("El area del triangulo es: ", res)
elif opcion == "C" or opcion == "c":
    pi = 3.141592
    radio = int(input("radio: "))
    res = pi * radio
    print("El area del circulo es: ", res)

"""

"""
EJERCICIO 7

Escriba un programa que pida ingresar 3 numeros
y me diga cual es el mayor de los 3 ingresados


"""
"""
n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))

mayor = 0

if n1 > n2 and n1 > n3:
    print(n1, " es el mayor")
else:
    if(n2 > n3):
        print(n2, " es el mayor")
    else:
        print(n3, " es el mayor")
"""
