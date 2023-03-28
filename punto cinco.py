#Imprimir el factorial de un número natural n dado.
n: int
m: int
fact: int
n = int(input("Insertar valor de n"))
m = 1
fact = 1
if n<0:
    print("No es posible calcular el factorial de " + str(n))
else:
    while m <= n:
        fact = fact*m
        m = m+1
    print("El factorial de " + str(n) + " es " + str(fact))