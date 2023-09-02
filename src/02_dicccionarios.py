nombre_dic = {"clave": "valor"}

diccionario = {"nombre": "Victor", "edad": 23}
print(diccionario)

# ver el valor de una clave especifica
print(diccionario["nombre"])
print(diccionario["edad"])

# modificar elementos
datos_personales = {"pais": "Italia", "ciudad": "Roma"}
datos_personales["ciudad"] = "Milan"
print(datos_personales)

# funcionalidades de un diccionario
datos = {"jose": 18, "david": 23, "camila": 19, "maria": 32}
datos.update({"raul": 33})  # actualizar el dict añadiendo un nuevo valor
print(datos)

# eliminar un elemento por su clave
del datos["david"]
print(datos)

# crear una lista a partir de un diccionario y sus claves
estudiantes_dict = {'jose': 18, 'camila': 19, 'maria': 32, 'raul': 33}
nombres = list(estudiantes_dict.keys())
print(nombres)
nombres.sort()
print(nombres)

# recorrer el diccionario usando una lista
for e in nombres:
    print(" : ".join((e, str(estudiantes_dict[e]))))
