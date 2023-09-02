# los elementos de una tupla no se pueden modificar
tuplas = (0, 1, 2, 3, 4, 5,)
print(tuplas)

# devuelve error, porq no puede ser modificado
# tuplas[0] = 1000

# en lista se pueden modificar
listas = [0, 1, 2, 3, 4, 5, ]
listas[0] = 1000
print(listas)

# combinar
tuplas_a = (0, 1, 2, 3, 4)
tuplas_b = ("a", "b", "c")
print(tuplas_a + tuplas_b)

# replicar n veces
tuplas_c = ("python") * 4
print(tuplas_c)

# contar elementos repetidos
tupla = (1, 5, 6, 8, 6, 5, 7, 5)
repetido = tupla.count(5)
print(repetido)

# encontar el primer elemento
tupla = (1, 5, 6, 8, 6, 5, 7, 5)
primero = tupla.index(5)
print(primero)

# modificar una tupla, con conversion
x = ("rojo", "amarillo", "verde")
y = list(x)
y[1] = "negro"
x = tuple(y)
print(x)
