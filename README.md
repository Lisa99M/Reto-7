# Reto-7
### Punto 1 
Código:
```
#Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
numero: int 
numero = 1
while (numero <= 100):
    print(str(numero) + "y" + str(numero**2)) 
    numero = numero +1
print("Fin")
```
Diagrama de flujo:

### Punto 2
Código:
```
#Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
i: int
for i in range (1,1000):
    if i%2 != 0:
        print(i)
for i in range (2,1001):
    if i%2 == 0:
        print(i)
print("Fin")
```
Diagrama de flujo:

### Punto 3
Código:
```
#Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
n: int
n = int(input("Introducir valor de n>=2"))
for n in range (n,1, -1):
    if n%2 == 0: #comprobar si n es par
        print(str(n))
print("Fin")
```
Diagrama de flujo:

### Punto 4
Si las tasas de crecimiento anual de los países A y B son 2% y 3% respectivamente, esto significa que el incremento poblacional del país A es de 2 personas porcada 100 habitantes y el del B 3 personas por cada 100 habitantes. 
Código:
```
#En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18:9 millones. Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. Desarrollar un algoritmo para informar en que año la población del país B superará a la de A.
añoA: float = 25e6
añoB: float = 18.9e6
año: int
año = 2022

while añoA >= añoB:
    añoA = añoA*(1 + 0.02)
    añoB = añoB*(1 + 0.03)
    año = año + 1
print("En el año " + str(año) + " la población del país B superará a la de A")
print("Fin")
```

###Punto 5
Código:
```
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
```

###Punto 6
Código:
```
#Implementar un algoritmo que permita adivinar un número dado de 1 a 100, preguntando en cada caso si el número es mayor, menor o igual.
adivinar_numero : int
import random
numero_desconocido = random.randint(1,100)
bandera : bool = True

while bandera:
    adivinar_numero = int(input("Insertar un número entre 1 y 100"))
    if numero_desconocido > adivinar_numero:
        print("Has introducido un número muy pequeño")
    elif numero_desconocido < adivinar_numero:
        print("Has introducido un número muy grande")
    else: 
        print("¡¡Has adivinado el número!!")
bandera = False 
```

###Punto 7
Código:
```
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
```

###Punto 8
Código:
```
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
```
_Final final_
