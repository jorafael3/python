
"""

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
