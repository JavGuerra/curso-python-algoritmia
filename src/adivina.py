import random 

def pedir_numero():
    while True:
        numero = input("Dime un numero entero: ")
        if numero.isnumeric():
            return int(numero)
        else:
            print("Error: intenta de nuevo")

def juego():
    numero_aleatorio = random.randint(1, 10)
    adivinado = False

    while adivinado == False:  # not adivinado

        numero = pedir_numero()
    
        if numero == numero_aleatorio:
            print("¡Correcto! El número era", numero_aleatorio)
            adivinado = True

        elif numero < numero_aleatorio:
            print("El número es demasiado bajo, intenta de nuevo.")
        else:
            print("El número es demasiado alto, intenta de nuevo.")

