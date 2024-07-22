# Funciones

# Definición
def saludo():
    print("¡Hola, Mundo!")

# Uso
saludo()

# Parámetros
def saludo(nombre):
    print("Hola", nombre)

mi_nombre = "Pedro"
saludo(mi_nombre) # Hola Pedro


def colores(color1, color2):
    print("Colores favoritos: ", color1, color2)

colores("Rojo", "Azul")


def saludo(nombre, apellido):
    print("Hola", nombre, apellido)

saludo("Pedro", "Pérez")


def seleccion(opc1, opc2):
    entrada = input(f"Seleccione {opc1} o {opc2}")
    if entrada.lower() == opc1:
        pass
        return True
    else:
        pass
        return False

# alexa(seleccion("on", "off"))


# parámetros por omisión
def saludo(nombre, apellido = "Sin Nombre"):
    print("Hola", nombre, apellido)

saludo("Juan") # Hola Juan Sin Nombre   # Jon Doe / Joan Doe
saludo("Pedro", "Pérez") # Hola Pedro Pérez


# Caso en que falta un parámetro.
# Multiplicar dos números o un número por si mismo
def multiplicar(n1, n2 = None):
    if n2 == None: n2 = n1
    print( n1 * n2 )

multiplicar(5, 4)
multiplicar(5)


# retorno
def suma(numero1, numero2):
    return numero1 + numero2

resultado = suma(5, 4) # 9
print(resultado)


def adivina_nombre(nombre):
    return nombre == "Pepe"

resultado = adivina_nombre("Juan")  # True / False
print(resultado)

tu_nombre = input("Dime tu nombre")
resultado = adivina_nombre(tu_nombre) # True / False
print(resultado)


# posición: primero definir, luego usar, sino error
# print(suma(5, 4))
# def suma(numero1, numero2):
#     return numero1 + numero2


# paso de valores por referencia
def division(numero1, numero2):
    return numero1 / numero2

resultado = division(numero2 = 4, numero1 = 5)
print(resultado)


# Variables locales
def suma_cinco(numero):
    sumando = 5
    return numero + sumando

print( suma_cinco(9) ) # 14
#print(sumando) # Error, 'sumando' es una variable que sólo se usa en suma_cinco()


# Funciones llamadas dentro de otras funciones
# Función que convierte un número en otro mayor que diez
def mayor_que_diez(n):
    while n < 10:
        n = suma_cinco(n)

    return n

print( mayor_que_diez(2) ) #12


# Recursividad: Funciones que se llaman a si mismas
# Ojo: concepto avanzado. Sólo para vuestro conocimiento
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1) # recursivo

factorial(5) # 120


# Ejercicio: Crear una función que reciba dos números y nos devuelva el mayor.


# Ejercicio: Crear una función que reciba tres números e imprima su media.


# Crear una función que devuelva el 21% de IVA de una cantidad dada.


# Ejercicio: Crear una función que pida un número entero por pantalla y lo
# devuelva con return o genere un aviso de error, volviendo a pedir el número.

def pedir_numero():
    while True:
        numero = input("Dime un numero entero: ")
        if numero.isnumeric():
            return int(numero)
        else:
            print("Error: intenta de nuevo")


# Haciendo uso de la función anterior, crear otra función que muestre la tabla
# de multiplicar de un número dado.


# Usa la función de pedir un número entero para incorporarla al ejercicio
# de adivina un número.


# Crea una función que imprima una cadena de 21 espacios que empeice y termine con *

# Crea una función que imprima una cadena con 21 espacios, pero en medio debe tener un caracter #

# Crear una función que imprima una cadena como la anterior,
# pero cuando escribamos q el # se va a despalzar a la izquierda,
# y cuando pulsemos w se va a despalzar a la derecha.
