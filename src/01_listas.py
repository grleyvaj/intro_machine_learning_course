# posiciones de una lista comienza en 0
number_list = [1, 2, 3, ]
print(number_list)

str_list = ["uno", "dos", "tres"]
print(str_list)

mixta_list = [1, 2, 3, "python", "curso", 4.5, ["a", "b"]]
print(mixta_list)

# combinar listas
list_a = [1, "a", 3, 4, "c", ]
list_b = [6, 7, 8, 9, 10]
suma = list_a + list_b
print(suma)

# modificar valores usando la posicion
numbers = [1, 2, 3, 4, 5]
numbers[2] = "nuevo"
print(numbers)

# si se emplea -1 se añade en la ultima posicion, en este caso la posicion del numero 5 es la ultima
numbers = [1, 2, 3, 4, 5]
numbers[-1] = "nuevo"
print(numbers)

# conocer la cantidad de elementos de la lista
lista = [1, "a", 3, "b"]
print(len(lista))

# elementos de un rango de posiciones
numbers = [1, 2, 3, 4, 5]
print(numbers[2:3])

# elementos a partir de una posicion
print(numbers[2:])

# elementos hasta de una posicion
print(numbers[:2])

# insertar datos a la lista
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers.insert(2, "nuevo")  # posicion, dato
print(numbers)

# insertar datos al final de la lista
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers.append("nuevo")
print(numbers)

# añadir valores a una lista usando otra lista (juntar dos listas)
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = ["a", "b"]
lista.extend(lista2)
print(lista)

# ordenar lista
letras = ["def", "abc", "xyz"]
letras.sort()
print(letras)

# invertir lista
numeros = [2, 5, 8, 54, 3, 6, 78]
numeros.reverse()
print(numeros)

# conocer la posicion de un elemento
numeros = [2, 5, 8, 54, 3, 6, 78]
print(numeros.index(54))

# eliminar datos, pop elimina el ultimo y regresa el valor eliminado
numeros = [2, 5, 8, 54, 3, 6, 78]
print(numeros.pop())
print(numbers)
eliminar = numeros.pop(3) # eliminar dado una posicion
print(eliminar)
