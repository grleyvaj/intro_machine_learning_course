# cada elemento del conjunto es unico (sin duplicaciones)
# y debe ser inmutable (no se puede cambiar)

set = {1, 2, 3, 4.6, "pyton", ("w", "t")}
print(set)

set = {1, 2, 3, 4.6}
set.add(5)
print(set)

# se añaden elementos unicos, si existe no se añade
set.add(5)
print(set)

# eliminar todos elementos del conjunto
set.clear()
print(set)

# descartar uno
set = {1, 2, 3, 4.6}
set.discard(2)
print(set)

# para eliminar uno
set = {1, 2, 3, 4.6}
set.remove(2)
print(set)

# conjunto union sin repetirlos
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A.union(B))
print(A | B)

# conjunto interseccion son los comunes
print(A.intersection(B))
print(A & B)

# diferencia entre conjuntos
print(A.difference(B))
print(A - B)
print(B - A)

# diferencia simetrica, union menos la interseccion
# q es lo mismo q la suma de las diferencias
print(A ^ B)

