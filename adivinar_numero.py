"""
ADIVINA EL NÚMERO
Objetivo:
Practicar el uso de while, break y continue en un juego interactivo.

Descripción:
El programa genera un número aleatorio entre 1 y 10, se requiere adivinarlo. Si el número ingresado no está entre 1 y 10, el programa muestra un mensaje y utiliza continue para pedir un nuevo intento. Si adivinan correctamente, el programa usa break para terminar el bucle.
"""

# Variable con un número "aleatorio"
random_number = 3

# Título al correr el código
print("¡ADIVINA EL NÚMERO!\nEstoy pensando un número entre el 1 y el 10. ¿Puedes adivinar cuál es?")

# Comienzo del ciclo
while True:
    write_number = int(input("Ingresa el número: "))
    
    # En caso de escribir números menores a 1 y mayores a 10, se nos pedirá ingresar nuevamente un número válido
    if write_number < 1 or write_number > 10:
        print("Debes escribir un número entre el 1 y el 10. Intenta nuevamente.")
        continue
    
    # Si el número ingresado es igual al número "aleatorio", se gana el juego
    if write_number == random_number:
        print("¡Has adivinado! ¡Felicidades! ♥")
        
    # Si el número ingresado no es igual al número "aleatorio", se pierde el juego
    if write_number != random_number:
        print("¡No has adivinado! ¡Has perdido! :(")
    
    # Si quiere volver a intentarlo, se reiniciará el ciclo desde el principio, sino el juego finalizará.
    try_again = input("¿Deseas volver a intentarlo? [S/N]: ").upper()
    if try_again == "S":
        continue
    
    else:
        print("¡Te esperamos nuevamente para volver a jugar!")
        
    break