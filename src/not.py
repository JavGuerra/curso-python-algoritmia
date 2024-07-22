cafe = False

cafe = bool(int(input("Has tomado café: 0, 1")))

if not cafe: # café es falso, pero (not café) es verdadero
    exit("dormido")
print("despiesto")


cafe = input("Has tomado café: S, N")

if not cafe.upper() == "S":
    exit("dormido")
print("despiesto")


numero = 12
if not (numero == 12):
    print("No concide")


numero = 12
if numero != 12:
    print("No concide")


numero = input("Dime un núnero")

# numero.isnumeric() -> True o False

if numero.isnumeric():
    print("Todo bien")
else:
    print("No es un número")


if not numero.isnumeric():
    exit("No es un número")
# resto de instrucciones


# Ejercicio: Preguntar al usuario si tiene coche o moto y gasolina
# imprimir mensajes de error si no tenemos medio de desplazamiento o no tenemos gasolina.
# not puede ser !=


tiene_coche = input("¿Tienes coche? (Sí/No): ")
tiene_moto = input("¿Tienes moto? (Sí/No): ")
tiene_gasolina = input("¿Tienes gasolina? (Sí/No): ")

# if tiene_coche.lower() != "sí" and tiene_moto.lower() != "sí":
#    print("Error: No tienes ningún medio de desplazamiento válido.")

if not tiene_coche.lower() == "sí" and not tiene_moto.lower() == "sí":
    print("Error: No tienes ningún medio de desplazamiento válido.")
    
if tiene_gasolina.lower() != "sí":
    print("Error: No tienes gasolina.")



asistencia = False

if not asistencia:
    print("Su hijo no ha asistido a clases. Gañán.")

if asistencia != True:
    print("Su hijo no ha asistido a clases. Gañán.")