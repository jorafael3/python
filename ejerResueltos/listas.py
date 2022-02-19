"""

Ejercicio 1

Escribir un programa que pregunte el correo electrónico del usuario en la consola 
y muestre por pantalla otro correo electrónico con el mismo nombre 
(la parte delante de la arroba @) pero con dominio cartimex.com

correo = input("correo: ")
correo = correo.split("@")[0]
correo = correo+"@cartimex.com"
print(correo)

"""

"""
Ejercicio 2

Escribir un programa que pregunte al usuario 3 números de la lotería de 5 digitos, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
y seleccione un ganador al azar

lista = []

n1 =  int(input("escriba n1: "))
n2 =  int(input("escriba n2: "))
n3 =  int(input("escriba n3: "))

lista.append(n1)
lista.append(n2)
lista.append(n3)

orden = sorted(lista)
orden.reverse()
print(orden)

"""

"""
Ejercicio 2

Escribir un programa que pregunte al usuario su nombre, edad, y teléfono 
y lo guarde en un diccionario. 
Después debe mostrar por pantalla el mensaje:

<nombre> tiene <edad> años, y su número de teléfono es <teléfono>.


nombre =  input("escriba nombre: ")
edad =  input("escriba edad: ")
telefono =  input("escriba telefono: ")


datos = {"nombre":nombre,"edad":edad,"telefono":telefono}

nom = datos["nombre"]
ed = datos.get("edad")
tel = datos.get("telefono")

print(nom + " tiene " +ed +" años y su telefono es "+ tel)

"""

"""
Ejercicio 3

Escribir un programa que guarde en una variable el diccionario 
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si 
la divisa no está en el diccionario.


monedas = {'euro':'€', 'dollar':'$', 'yen':'¥'}
mon = input("escriba divisa: ")

if mon in monedas:
    print("moneda: ", mon)
    print(monedas[mon])
else:
    print("moneda no esta")

"""

"""
Ejercicio 4

Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el 
precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe 
mostrar un mensaje informando de ello.
----------------------
   Fruta   |   Precio
----------------------
| Plátano	|  1.35  |
| Manzana	|  0.80  |
| Pera	    |  0.85  |
| Naranja	|  0.70  |

frutas = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
fruta = input('¿Qué fruta quieres? ')
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '$')
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")
    
"""
