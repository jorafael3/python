# **** Arithmetic Operators ***
import math  # Libreria math


a = 7
b = 2

suma = a + b
resta = a - b
mult = a * b
div = a / b
divfloor = a//b  # floor division
mod = a % 2  # residuo
exp = a**b  # exponente

c = 3.8
f = round(c)
d = math.ceil(c)
e = math.floor(c)


# **** entrada de texto por teclado

# LA ENTADA DE TEXTO ES UN STRING
# SI SE QUIERE INGRESAR UN NUMERO HAYQ UE CONVERTIRLO A INTEGER, FLOAT, ETC

#operador de concatenacion + 


texto = input("ingrese nombre: ")
print("Su nombre "+texto)


numero = input("numero 1: ")
numero2 = input("numero 2: ")

print("suma: ", int(numero)+int(numero2))
