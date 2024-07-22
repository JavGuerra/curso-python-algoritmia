
tabla = 5
i = 1
while i <= 10: # condición a cumplir
    print (f"{tabla} x {i} = {tabla * i}") # 5 x 2 = 10
    i = i + 1


# ejercicio tabla de multiplicar con for
tabla = 5

for i in range(1, 11): # rango, el número siguiente al que queremos que se pare
    print (f"{tabla} x {i} = {tabla * i}")

# ejercicio listar de cinco en cinco
for i in range(0, 101, 5):
    print(i)


# ejercicio adivina el numero 5
numero = 0
while numero != 5:
    numero = int(input("dime un número"))


'''
Ejercicio para usar el bucle «for»:
Hacer un programa que simule tirar tres dados, muestre el valor de cada dado y
sume el valor de los tres en cada tirada. Luego, mostrar el resultado de la suma
de los tres dados.
'''

import random

total = 0

for i in range(3):
    dado = random.randint(1, 6)
    print(f"Tirada {i + 1}: {dado}")
    total += dado # total = total + dado

print(f"En total has obtenido {total} punto(s).")


# ejercicio listar caracteres de una cadena
for i in "¡AMIGO!":
    print ("dame una ", i)


# Ejercicio sustituir vocales de una cadena por la letra i
texto = ""
for i in "¡AMIGO!":
    if i == "A" or i == "E" or i == "O" or i == "U":
        i = "I"
    texto = texto + i # concatenar

print(texto) # ¡IMIGI!


# ejercicio uso de listas
dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes"]
for i in dias_semana:
    print (i, "es un día laborable.")


# ejercicio uso de diccionario
dias_semana = {"lunes": 1, "martes": 2, "miércoles": 3, "jueves": 4, "viernes": 5}
for i in dias_semana:
    print (f"El orden del {i} es: {dias_semana[i]}")

