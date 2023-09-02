# generar un rango de #s enteros entre el entero inicial y el final

print(list(range(0, 7)))

for i in range(0, 7):
    print("El valor de i es: ", i)

for i in range(0, 7, 2):  # con paso 2
    print(i, end="- ")

for num in range(10):
    for i in range(num):
        print(num, end=" ")
    print()

# recorrer un rango pero a la inversa
for i in reversed(range(0, 10)):
    print(i)

generar_lista = list(range(1,8))
print("lista", generar_lista)
