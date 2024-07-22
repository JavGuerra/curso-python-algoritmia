import modulo
# from modulo import suma, resta, multiplica, divide
# from modulo import *
# más info: https://docs.python.org/es/3/tutorial/modules.html

a = 5
b = 4
j = 12
p = 3

while True:
    opt = input("""\nCalculadora:
1. Suma
2. Resta
3. Multiplicación
4. División
0. Salir
Seleccione una opción: """)

    if not opt.isnumeric():
        print("Opción incorrecta")
        continue
    opt = int(opt)

    match opt:
        case 1:
            print( "suma: ", modulo.suma(j, p) )
        case 2:
            print( "resta", modulo.resta(a, b) )
        case 3:
            print ( "multiplicación", modulo.multiplica(a, b) )
        case 4:
            print( "división", modulo.divide(a, b) )
        case 0:
            exit()
        case _:
            print("Opción incorrecta")
