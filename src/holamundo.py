'''
autor: Javier Guerra
Fecha: 21-6-2023
version: 1.0.0
'''

print('¡Hola, Mundo!')
print("let's go!")
print('let\'s go!')
print('"Máquina del\ntiempo"')
print("hola", "mundo")

veces = 5

print("pppppppp  " * int(veces)) # El int() no es necesario si veces es entero
print("p       p " * int(veces))
print("pppppppp  " * int(veces))
print("p         " * int(veces))
print()
print("veces", veces)
print()
print("'veces' contiene", veces, "que permite multiplicar texto.")
print("'veces' contiene" + str(veces) + "que permite multiplicar texto.")

# str(5) -> "5"


numero1 = 8
numero2 = "8"

print(str(numero1) + numero2) # concatenar: unir cadenas de texto -> "88"
print(numero1 + int(numero2)) # sumar valores enteros -> 16

numero3 = int(numero2)
numero4 = str(numero1) # cadena

print (type(numero2), type(numero3)) # str e int

# print(int("Hola")) # Da error porque Hola no tiene forma de número

print(f"número: {numero1}") # f-string
print(f"número: numero1")
print("número: {}".format(numero1)) # método

diametro = 22
print(f"el diametro es: {diametro} metros")
print("el diametro es: ", str(diametro), "metros")

numero1 = 8.5555555555
numero2 = 8
print(type(numero1), type(numero2)) # float e int

print(float(numero2)) # devuelve un número en punto flotante -> float
print(int(numero1)) # Devuelve la parte entera -> int

decimales = round(numero1, 2) # 8.56
print(decimales)  # formatea el número a un númer ode decimales

coche = True      # boolenana (bool): True = 1 ó False = 0

print(type(coche))

print(int(coche)) # 1 ó 0

# identación

for i in "¡Python!":
    print("¡Dame una ", i, "!")   # texto indentado. Si no, error.


# Variables
Cosas = 2
cosas = 1 # No es igual a la anterior. Mayúisculas y minúsculas.
España = "¡Olé!" # No se suelen usar caracteres que no estén en el teclado inglés
camion = "8 ruedas" # No se suelen acentuar las variables
mi_casa = "teléfono" # descripción del nombre de la variable: snake case
miCasa = "teléfono"  # camel case
MiCasa =  "teléfono" # Pascal case
# Mi-Casa = "teléfono" # Kebab case No funciona en Python


# Operaciones matemáticas
# + - * /  // % **

n1 = 12
n2 = 5

# Prueba de operaciones
print("Suma", n1 + n2)
print("Resta", n1 - n2)
print("Multiplicación", n1 * n2)
print("División", n1 / n2)
print("Div. entera", n1 // n2) # Parte entera de la división
print("resto", n1 % n2) # Resto de la división
print("Potencia", n1 ** n2)

# precedencia de operadores
calculo = ( (2 + 4) * 8 ) ** 3

# ¿Cuántos años quedan para tener 50 años partiendo de un dato menor de 50, que es la edad actual?
edad = 28
limite = 50
print(limite - edad)

# ¿Cuantos metros son x kilómetros?
kilometros = 10 # un  valor a decidir por el usuario
metros = kilometros * 1000
print(f"{kilometros}Km son {metros}m")

# ¿Cuantos kilómetros son x metros?
metros = 100000
kilometros = metros / 1000
print(f"{metros}m son {kilometros}km")

# ¿hipotenusa al cuadrado?  # a (hipotenusa) cuadrado = b cuadrado + c cuadrado (catetos)
cateto1 = 4
cateto2 = 6
hipotenusa_al_cuadrado = cateto1 ** 2 + cateto2 ** 2
print("hipotenusa =", hipotenusa_al_cuadrado)
print(f"hipotenusa = {cateto1 ** 2 + cateto2 ** 2}")

# Pecedencia de operadores matemáticos
print(2 + 5 * 8)
print ((2 + 5) * 8)

# Manda un saludo a una persona cuyo nombre sea x
nombre = "Vanesa"
print(f"Hola, {nombre}!")

n1 = 8
n2 = 3.5
print(n1 * n2) # Resultado tipo punto flotante

print('''
    autor: Javier Guerra
    Fecha: 21-6-2023
    version: 1.0.0
''')

print('''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna
aliqua. Ut enim ad minim veniam, quis nostrud exercitation
ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit
esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia
deserunt mollit anim id est laborum.''')

# input

print("Dime tu nombre")
nombre = input() # Se obtiene una cadena de texto
print("Hola", nombre)

# Ejercicio: pedir la edad y calcular cuanto falta para 50
print("Dime tu edad")
edad = input()  # pide el dato por teclado y guárdalo en edad "40"
print("Tu edad es: " + edad) # Concatenar
print(50 - int(edad))

# Pasar de kilómetros a metros
kilometros = input("Dime los kilómetros ")
metros = float(kilometros) * 1000
print(f"{kilometros}Km son {metros}m")

radio = float(input("Escribe el radio de la circunferencia: "))
print(type(radio), radio)

# Calcular el IVA de un producto que tiene un precio X. IVA 21%
precio = float(input("Introduzca el precio del producto: "))
iva = round(precio * 21 / 100, 2) # precio * 0.21
print(f"El IVA de {precio} es {iva}.")

