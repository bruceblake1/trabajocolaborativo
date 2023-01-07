#3.	Elabore un programa que le solicite al estudiante la cantidad de 
# lunas que hay en el planeta saturno,y le repita la pregunta hasta que responda de manera correcta
#las lunas de Saturno son 53
lunas_saturno=53
numero=int(input("Ingrese el número de lunas de Saturno: "))
while (numero!=lunas_saturno):
    if(numero!=lunas_saturno):
        numero=int(input("Ingrese correctamente el número de lunas de Saturno: "))
print("Averiguaste el numero de lunas de Saturno")
        