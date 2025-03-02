import random

matriz = [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]

# Mostrar la matriz generada
print("Matriz original:")
for fila in matriz:
    print(fila)

# Función para ordenar
def ordenar_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[fila][j] > matriz[fila][j+1]:
                # Intercambiar elementos
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]

# Pedir al usuario
fila_a_ordenar = int(input("Ingresa el número de fila que deseas ordenar (0-2): "))

# Ordenar
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz y la fila
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)