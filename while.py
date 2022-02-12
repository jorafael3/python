a, b = 0, 1
while a < 1000:
     #print(a, end=',')
     a, b = b, a+b

a = "hola,  + como + estas"
b = a.split("+")
c = "hola"

if a in b:
    print(a)