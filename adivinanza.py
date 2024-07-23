
import random


numero_secreto = random.randint(1,100)
cant_intentos = 0
cant_max_intentos = 5
adivinado = False

print("¡Bienvenido al juego de adivinanzas!")

while not adivinado:
    if not cant_intentos < cant_max_intentos:
        print("¡Game over! No has podido adivinar el número secreto")    
        break

    entrada = input("Introduce un número del 1 al 99: ")
    numero = int(entrada)

    if numero == numero_secreto:
        print("¡Felicidades, has adivinado el número secreto")
        adivinado = True
    elif numero < numero_secreto:
        print("El número ingresado es menor al número secreto")
    else :
        print("El número ingresado es mayor al número secreto")

    cant_intentos += 1




