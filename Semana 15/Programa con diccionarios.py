#Diccionario con información personal
informacion_personal = {"nombre": "Angela","edad": 21,"ciudad": "Tena"}

#Muestro el diccionario original
print("Diccionario original:")
print(informacion_personal)
print()

# Modifico el valor de la ciudad
informacion_personal["ciudad"] = "Manta"
print("Cambio de ciudad:")
print(informacion_personal)
print()

# Agrego la profesión
informacion_personal["profesion"] = "Estudiante"
print("Cambio de profresión:")
print(informacion_personal)
print()

# Verifcación de existencia del númeor de telefono
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0981334703"
print("Después de verificar y agregar teléfono:")
print(informacion_personal)
print()

# 4. Eliminar la edad
del informacion_personal["edad"]
print("Eliminación de edad:")
print(informacion_personal)
print()

#Output del diccionaro final con los nuevos cambios
print("Diccionario final:")
print(informacion_personal)