num=1
print("¿Cuantas numeros ingresara? ")
cant= int(input())
sum= 0
while num <= cant:
    print("Ingrese el número: ", num)
    numero = float (input())
    sum+=numero
    num+=1
print("La suma de los numeros es: ", sum)