from despues.ejerim import suma, menuSum,MostrarArreglo



def menu():
        print('\n')
        print("*************************")
        strs = ('Enter 1 for addition\n'
                'Enter 2 for subtaction\n'
                'Enter 3 for multiplication\n'
                'Enter 4 for division\n'
                'Enter 5 for AgregarElemento\n'
                'Enter 0 to exit : ')               
        choice = input(strs)
        return int(choice) 



def resta(a,b):
    print(a-b)

def multi(a,b):
    print(a*b)

def div(a,b):
    try:
        print(a/b)
    except ZeroDivisionError as e:
        print("no se puede dividir para 0")


def sis():
    while True:          #use while True
        choice = menu()
        if choice == 1:
            #suma(int(input("Primer numero: ")),int(input("segundo numero: ")))
            menuSum()
        elif choice == 2:
            resta(int(input("Subtract this: ")),int(input("from this: ")))
        elif choice == 3:
            multi(int(input("Multiply this: ")),int(input("by this: ")))
        elif choice == 4:
            div(int(input("Divide this: ")),int(input("by this: ")))
        elif choice == 5:
            MostrarArreglo()
        elif choice == 0:
            break


sis()