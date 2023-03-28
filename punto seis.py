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