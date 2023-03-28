#Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
numero: int 
numero = 1
while (numero <= 100):
    print(str(numero) + "y" + str(numero**2)) 
    numero = numero +1
print("Fin")