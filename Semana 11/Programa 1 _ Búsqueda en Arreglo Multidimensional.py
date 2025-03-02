import random

matriz = [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]

print("Matriz generada:")
for fila in matriz:
    print(fila)

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Devuelve la posición (fila, columna)
    return None  # Si no se encuentra el valor

# Valor a buscar
valor_buscado = int(input("Ingresa el valor que deseas buscar (1-9): "))

# Búsqueda
resultado = buscar_valor(matriz, valor_buscado)

# Mostrar el resultado
if resultado:
    print(f"El valor {valor_buscado} se encontró en la posición {resultado}")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")