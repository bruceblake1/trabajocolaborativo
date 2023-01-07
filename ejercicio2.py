#2.	Elabora un programa que te permite introducir números, y si los números están en 
# el rango 20 y 40, te indique “Estas en rango” y si no es así, que te señale “No estás en el rango”

while True:
    num=int(input("Escribe un numero: "))
    if(num>=20) and (num<=40):
        print("Estas en rango")
    else:
        print("No estas en el rango")