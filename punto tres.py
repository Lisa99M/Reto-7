#Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
n: int
n = int(input("Introducir valor de n>=2"))
for n in range (n,1, -1):
    if n%2 == 0: #comprobar si n es par
        print(str(n))
print("Fin")