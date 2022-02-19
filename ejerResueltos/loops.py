"""
Ejercicio 1
Escribir un programa que pida al usuario una palabra y la muestre por
pantalla 10 veces con su numero



palabra = input("palabra: ")

for n in range(10):
    print(str(n+1) + " - "+ palabra)


"""


"""
Ejercicio

Escribir un programa que pida al usuario un número entero positivo y
muestre por pantalla todos los números impares desde 1 hasta ese número


numero = int(input("numero :"))
for n in range(1,numero+1,2):
    print(n)
"""


"""
Ejercicio 3

Escribir un programa que pida al usuario un número entero y muestre por
pantalla un triángulo rectángulo como el de más abajo, de altura el número
introducido.

altura = 6

*
* *
* * *
* * * *
* * * * *
* * * * * *

numero = int(input("numero :"))
acu =""
for n in range(1,numero+1,1):
    acu = acu + "* "
    print(acu)


"""


"""

Ejercicio 4

Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1

numero = int(input("numero :"))
acu = ""
for n in range(1,numero+1,2):
    acu = str(n) + " "+acu
    print(acu)


"""

"""

ingresar el nombre y edad de 2 personas
-guardarlos en una lista
-volver a imprimirlos de la sgut manera

<nombre> 1 tiene <edad> años
-

for n in range(2):

    nombre = input("Nombre: ")
    edad = input("edad: ")
    dict = {"nombre": nombre, "edad": edad}
    datos.append(dict)

print(datos)

"""

"""

Los siguientes datos fueron extraidos de una base de datos

se pide imprimir el sgte reporte

-contar la cantidad de registros 
-si son mayores de edad imprimir su nombre y su genero
-si son menores imprimir solo su nombre y un mensaje que indique que es menor
-cuantas son mayores de edad y cuantas menores de edad 
-cuantos son hombres y cuantas mujeres hay 
-si son mayores y es Hombre agregar un nuevo registro hobby peliculas
-si son mayores y es Mujer agregar un nuevo registro hobby anime
-si son menores y agregar un nuevo registro hobby caricaturas

datos = [{'nombre': 'priscila', 'edad': '18', "genero": "F"},
         {'nombre': 'erika', 'edad': '28', "genero": "F"},
         {'nombre': 'jorge', 'edad': '17', "genero": "M"},
         {'nombre': 'christian', 'edad': '30', "genero": "M"},
         {'nombre': 'ivan', 'edad': '10', "genero": "M"}]

cantidad = len(datos)
mayores = 0
menores = 0
hombres = 0
mujeres = 0


for dato in datos:
    edad = int(dato["edad"])
    nombre = dato["nombre"]
    genero = dato["genero"]

    if(edad >= 18):
        mayores += 1
        if(genero == "M"):
            dato["hobby"] = "peliculas"
        elif(genero == "F"):
            dato["hobby"] = "anime"
    elif edad < 18:
        menores += 1
        dato["hobby"] = "caricatura"


    if(genero == "M"):
        hombres += 1
    elif(genero == "F"):
        mujeres += 1

        # print(nombre+" es mayor de edad")
print(cantidad, " registros")
print("************************************")
print(mayores, " son mayores de edad")
print(menores, " son menores de edad")
print("************************************")
print(hombres, " son Hombres")
print(menores, " son Mujeres")
print("************************************")
print(datos[0]["hobby"])

"""


datos = [
    {
        'nombre': 'priscila',
        'id': '01',
    },
    {
        'nombre': 'erika',
        'id': '02',
    },
    {
        'nombre': 'jorge',
        'id': '03',
    },
    {
        'nombre': 'christian',
        '04': '30',
    },
    {
        'nombre': 'ivan',
        'id': '05',
    }]
