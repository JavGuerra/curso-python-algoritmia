def linea(pre):
    if pre >= 0 and pre <= 20:
        post = 20 - pre
        print(f"*{' ' * pre}#{' ' * post}*")
    else:
        print("error")

posicion = 10

while True:
    linea(posicion)

    mov = input()
    
    if mov.lower() == "q":
        if posicion >  0: posicion -= 1
    elif mov.lower() == "w":
        if posicion < 20: posicion += 1
    else:
        exit()

