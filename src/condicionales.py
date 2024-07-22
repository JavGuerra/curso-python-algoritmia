# ejercicio

booleano = False
if booleano: print("boolenano es True")

pulsador = bool( int( input("Encender o apagar: 1 ó 0: ") ) ) # "1", "0" -> 1, 0 -> True, False
print(pulsador)
if pulsador: print("Luz encendida")


pulsador = input("Encender o apagar: 'on' o 'off': ")
if pulsador == "on":
    pulsador = True
else:
    pulsador = False
print(pulsador)
if pulsador: print("Luz encendida")

# alternativa
pulsador = input("Encender o apagar: 'on' o 'off': ")
if pulsador == "on": 
    print("Luz encendida")


# Ejercicio: Preguntar al usuario si se vaa de vacaciones, y si es sí, imprimir "Buen viaje!"


if booleano:
    print("boolenano es True")
else:
    print("boolenano es False")


# ejercicio

nombre = "Javier"
nuevo_nombre = input ("Adivina mi nombre: ")
if nombre == nuevo_nombre: # then
    print ("¡Acertaste!")
else:
    print ("No acertaste...")


# ejercicio

edad = 54
nueva_edad = int(input ("¿Qué edad tengo? "))

if edad == nueva_edad:
    print("¡Acertaste!")
else:
    if edad > nueva_edad:
        print ("Te has quedado corto.")
    else:
        print ("Te has pasado.")


# elif sustituye a else + if

if edad == nueva_edad:
    print ("¡Acertaste!")
elif edad > nueva_edad:
    print ("Te has quedado corto.")
else:
    print ("Te has pasado.")


opcion = 1

if opcion == 1:
    pass
elif opcion == 2:
    pass
elif opcion == 3:
    pass
else:
    pass


if opcion == 1:
    pass
else:
    if opcion == 2:
        pass
    else:
        if opcion == 3:
            pass
        else:
            pass


# ejercicio Lotería

comprar = True # booleano True / False
tocar   = False
cambiar = True

# if (verdadero) entonces...
#    True       False      True
if (comprar and tocar and cambiar):
    print ("¡Millonario!")
else:
    print ("Me quedo igual...")


coche = True
moto = False
gasolina = True

if (coche or moto) and gasolina:
    print("Nos vamos de vacaciones")
else:
    print("me quedo en Tierra")


# not

# True -> not True -> False
# False -> not False -> True

if not (comprar and tocar and cambiar):
    print ("Sigue jugando")
else:
    print ("¡Fiesta!")


cafe = False
if cafe:
    print("despierto")
else:
    print("dormido")


cafe = False
if not cafe:
    print("dormido")
print("despiesto")


login = False
if not login:
    exit("No se ha hecho login")
print("Bienvenido")


login = False
# El resultado de not login es True
#  ---True-- si es False, le da el valor inverso
# El not NO cambia el valor de la variable, sino que opera para invertir el valor
if not login: print("Error de login")
pass # sigo
pass



cafe = input("¿Has tomado café? (S/N): ")
if not (cafe.lower() == "s" or cafe.lower() == "sí" or cafe.lower() == "si"):
    exit ("ZzZzZz ve a dormir")
print("Estamos listos para empezar.")

# match

opt = 1

if opt == 1:
    print(1)
elif opt == 2:
    print(2)
elif opt == 3:
    print(3)
else:
    print("Otro") 


match opt:
    case 1:
        print(1)
    case 2:
        print(2)
    case 3:
        print(3)
    case _:
        print("Otro")


# ejercicio: hacer el menú de una aplicación con cinco opciones.
# Pedor al usuario que introduzca por consola un número del 1 al 5. 
# Cualquier otro número o dato mostrará un mensaje de aviso.

# ¿Cómo implementarías una opción para salir del programa?


# while

numero = 1               # iterator
while numero <= 10:      #si se cumple la condición, se repite
    print (numero)
    numero += 1          # numero = numero + 1

'''
numero = 1
True
1
1 + 1 = 2
True
2
2 + 1 = 3
True
3
3 + 1 = 4

...

9 + 1 = 10
True
10
10 + 1 = 11
False
Se acabó el bucle
'''


texto = "aaaaa"   # "a" * 5
nuevo = ""

while not texto == nuevo:
    nuevo = nuevo + "a"

opt = ""
while not opt == "salir":
    opt = input("Elija una opción 1..3 o salir")
    match opt:
        case "1":
            print(1)
        case "2":
            print(2)
        case "3":
            print(3)
        case "salir":
            print("salir")
        case _:
            print("Otro")


# While

condicion = True

while condicion == True:
    pass
    # bloque de opciones
    # condición de salida que cambia


# Imrpime los núemros del 1 al 10

n = 1
while n <= 10:
    print(n)
    n += 1

ganar = False
numero = 0
tu_numero = 1
while not ganar:
    print()
    # input tu_numero
    # if tu_numero == numero:
    #    ganar = True


# ejercicio tabla de multiplicar

tabla = 5
i = 1
while i <= 10:
    print (f"{tabla} x {i} = {tabla * i}")  # 5 x 2 = 10
    print(tabla, "x",  i, "=", tabla * i)
    i = i + 1


# Ejercicio, hacer un bucle que imprima los números del 50 al 1, y que cuando el número sea igual a
# 50 o 40 o 30 o 25, imprima el mensaje "número!"

numero = 50

while numero > 0:

    if numero == 50 or numero == 40 or numero == 30 or numero == 25:
        print("¡número!")
    else: 
        print(numero)
    
    numero -= 1


# ejercicio: pedir por consola un número del 1 al 10 para imprimir su tabla de multiplicar
# Usa tabla.isnumeric() para comprobar si el dato recibido es un número. Sino, salir con exit()


# Ejercicio: Adivina un número aleatorio del 1 al 10.
# Debes solicitar el número hasta que el usuario acierte.
# Debes indicar, cada vez, si el número introducido es más bajo o más alto que el numero aleatorio.

# Ejercicio: Cuando tengas terminado el ejercicio anterior, usa .isnumeric() para comprobar
# si el dato recibido es un número. Sino, indicarlo con un mensaje de error y volver a pedirlo.
