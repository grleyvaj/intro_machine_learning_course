def mi_funcion(nombre: str, edad: int) -> None:
    print("Hola, mi nombre es " + nombre + " y tengo", edad)


mi_funcion("Gloria", 33)


def suma(n1, n2: int) -> None:
    return n1 + n2


print(suma(2, 4))

x = 80
print("variable global", x)


def mi_num():
    y = 50
    z = 50 + x
    print("variable local:", y)
    print("acceso a variables globales:", z)


mi_num()
