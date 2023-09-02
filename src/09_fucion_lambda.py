# lambda -> funcion anonima

def doble(x):
    return x * 2


print(doble(200))

# nombre: contenido de la funcion
calcular_doble = lambda x: x * 2
print(calcular_doble(200))

# aplicar lambda en filter (buscar los pares)
lista = [1, 5, 6, 78, 9, 5, 4, 67, 8, 24, 12]
lista_pares = list(filter(lambda x: x % 2 == 0, lista))
print(lista_pares)

# aplicar lambda en map (duplicar los elementos)
lista = [4, 5, 7, 98, 5, 2, 4, 6]
lista_doble = list(map(lambda x: x * 2, lista))
print(lista_doble)
