resultado = '1'

for i in range(2, 101):
    resultado += ', '
    
    x3 = i % 3 == 0  # True / False
    x5 = i % 5 == 0

    if x3 or x5:
        if x3: resultado += 'fizz'
        if x5: resultado += 'buzz'
    else:
        resultado += str(i)

print (resultado)
