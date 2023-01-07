#5.	Elabore una calculadora de suma y restas de dos números, el programa deberá seguir mostrado el menú.
#Opción 1: Suma
#Opión 2: Resta
respuesta=''
while respuesta!="n":
    print("***********")
    print("Calculadora")
    print("***********")
    print("Opcion 1: Suma")
    print("Opcion 2: Resta")
    opcion=int(input("Opcion a escoger: "))
    if (opcion==1):
        print("Escogiste suma")
    elif (opcion==2):
        print("Escogiste resta")
    #datos del usuario
    num1=int(input("Numero #1: "))
    num2=int(input("Numero #2: "))
    #variables
    respuesta=''
    suma=num1+num2
    resta=num1-num2
    if opcion==1:
        print("La suma es ",suma)
    elif opcion==2:
        print("La resta es ",resta)
    else:
        print("Escoge una opcion correcta.")

    print("Desea continuar?s/n: ")
    cambio=input('').lower()
    respuesta=cambio
print("Gracias por usar la calculadora")