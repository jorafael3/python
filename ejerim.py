
Arreglo = []

def menuSum():
    print('\n')
    strs = ('Enter 1 para sumar\n'
                'Enter 0 to exit : ')
    choice = int(input(strs))
    while True:          #use while True
        if(choice == 1):
            a = int(input("n1: "))
            b = int(input("n2: "))
            suma(a,b)
       
        elif(choice == 4):
            break


def Agregar(a):
    if(len(Arreglo) >= 5):
        print("Nose puede agregar, lleno")  
        menuSum()
    else:
        Arreglo.append(a)
        print("Elemento Agregado")



def suma(a,b):
    print("******************")
    print("La suma es: ",a+b)
    print("******************")
    return menuSum()



def MostrarArreglo():
    print('\n')
    strs = ('1.Agregar Elementos\n'
            '2.mostrar Todo\n'
            '3.mostrar posicion det\n'
            'Enter 4 to exit : ')
    a = int(input(strs))
    while True:          #use while True
        if(a == 1):      
            a = int(input("n: "))
            Agregar(a)
        elif(a == 2):
            print(Arreglo)
            break
        elif(a == 3):
            i = input("Igrese posicion");
            print(Arreglo[i])
            break
        elif(a == 0):
            break
