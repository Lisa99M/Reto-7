#Implementar el algoritmo que muestre los números primos del 1 al 100. nota: use funciones

def mostrar_primos(numero):
    list_of_primos = []
    for i in range (1,101):
        if numero % i != 0:
            list_of_primos.append(i)        
    return list_of_primos

numero = int(input("Ingrese un número entre 1 y 100: "))
if 1 <= numero <= 100:
    list_of_primos = mostrar_primos(numero)
    print("Los números primos del 1 al " + str(numero) + " son " + str(list_of_primos))
else:
    print("El número ingtresado no se encuentra dentro del rango del 1 al 100")