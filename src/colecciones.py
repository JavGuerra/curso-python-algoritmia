# Colecciones = tipos de datos

# lista

a = [1, 2, 3, 4]
b = list("1234") # objeto iterable
c = [5, "¡Hola, Mundo!", (1, 2), True, -1.5]
d = list()
e = []

print(b)
print(a[0]) # el valor inicial de la lista
print(a[-1]) # el valor final de la lista

a[2] = 1

a = [2, 4, 1, 3]
a.sort()
a.sort(reverse = True)

a.remove(2) # borra elemento concreto
a.pop(2) # borra elemento en la posición
a.pop() # borra último elemento
print(a)

# Unir listas
c = c + a

# Borrado por rebanadas
del c[2:5] # borra del índice 2 al 4
del c[-3:] # borra del índice antepenúltimo al final
del c[:] # borra todos los elementos
print(c)

a.clear() # borra todos los elementos
print(a)

# longitud
print( len(c) )

# iterar
for i in c:
    print(i)


# tupla (inmutable)

a = (5, "Hola mundo!", True, -1.5)
a = tuple()
a = ()


# set

unicos = set([3, 5, 6, 1, 5])
unicos = {3, 5, 6, 1, 5}
print(unicos)

print(5 in unicos)


# diccionario

# creación
d = {1: 'hola', 89: 'María', 'a': 'b', 'c': 27}
d = {}

d = dict()
d = dict(uno = 1, dos = 2, tres = 3)
d = dict({'uno' : 1, 'dos' : 2, 'tres' : 3})
d = dict([('uno', 1), ('dos', 2), ('tres', 3)])

# número de elementos
print( len(d) )

# Acceso
print( d['dos'] )
# print( d['cuatro'] ) # error, no existe el elemento

# ¿Existe?
print('uno' in d) # True

# Añadir
d['cuatro'] = 4
print(d)

# Modificar
d['uno'] = 1.0
print(d)

# Borrar
d.pop('uno') # uno
d.popitem()  # último
print(d)

d.clear() # todos
print(d)

# iterar
d = dict(uno = 1, dos = 2, tres = 3)

for e in d:
    print(e)

# claves
for k in d.keys():
    print(k)

# valores
for v in d.values():
    print(v)

# pares clave - valor
for i in d.items():
    print(i)


