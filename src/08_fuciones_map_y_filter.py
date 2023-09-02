# map -> ejecuta una funcion para cada elemento iterable

def multiplicar(n):
    return n * 5


lista = [1, 2, 3, 4, 5, 6, 7]
lista_map = list(map(multiplicar, lista))
print(lista_map)


def cursos(c):
    return c.upper()


tupla = ("php", "python", "java", "dart", "css",)
tupla_actualizada = tuple(map(cursos, tupla))

print(tupla_actualizada)


# filter -> crea un nuevo iterador a partir de un iterable existence
def impares(n):
    if n % 2 == 1:
        return n


lista = [1, 2, 3, 4, 5, 6]
lista_impares = list(filter(impares, lista))
print(lista_impares)
