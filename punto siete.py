#Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores.
def divisores_numero(numero):
    divisores = []
    for n in range(2,51):
        if numero % n == 0:
            divisores.append(n)
    return divisores

numero = int(input("Ingrese un número entre 2 y 50: "))
if 2 <= numero <= 50:
    divisores =  divisores_numero(numero)
    print("Los divisores de" + str(numero) + " son:" + str(divisores))
else:
    print("El número ingresado no se encuentra dentro del rango de 2 a 50.")