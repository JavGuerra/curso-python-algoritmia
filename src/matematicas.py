import random
import math

# numero aleatorio

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)

# Raíz cuadrada

print(math.sqrt(49)) # square root
print(7 * 7) # Comprobación

numero = float( input("Dime tu nçumero: ") )
print("Has puesto el número", numero)
raiz = math.sqrt(numero)
print(raiz)
print(round(raiz * raiz, 2), "=", numero) # Comprobación


# Opoeradores de asignación abreviados
# += -= *= **= /= //= %=

# multiplica la variable numero1 por si misma
numero1 = 5
numero1 = numero1 * numero1  # numero1 * numero1 -> numero1
print(numero1)

numero1 = 5
numero1 *= numero1
print(numero1)


# Multiplica numero1 por un número cualquiera y guarda el resultado en numero1

numero1 = 5
numero2 = 10
numero1 *= numero2 # numero1 = numero1 * numero2
print(numero1)


# Suma numero1 a un número cualquiera y guarda el resultado en numero1
numero1 = 5  # reseteo las variables
numero2 = 10
numero1 += numero2 # numero1 = numero1 + numero2
print(numero1)


# Buscando información en Internet, averigua
# cuantas veces cabe el planeta Tierra en el planeta Júpiter
# Guardar el resultado en la variable "jupiter"

jupiter = 1_431_281_810_739_360 # 1E25 Km3
tierra = 1_000_000_000_000 # datos redondeados
print(jupiter, tierra)

veces = jupiter / tierra
print(veces)

jupiter /= tierra # jupiter = jupiter / tierra
