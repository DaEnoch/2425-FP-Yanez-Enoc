ciudades = ["Tena", "Manta"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2  # Solo 2 semanas para simplificar

# Creo la matriz
# He colocado solo dos semanas por ciudad
#Cabe recalcar que la temperatura es en celcius
temperaturas = [
    [  # Tena
        [25, 26, 27, 28, 29, 30, 31], #Semana 1
        [24, 25, 26, 27, 28, 29, 30]    #Semana2
    ],
    [  # Manta
        [20, 21, 22, 23, 24, 25, 26],   #Semana 1
        [19, 20, 21, 22, 23, 24, 25]    #Semana 2
    ]
]

for i_ciudad, ciudad in enumerate(ciudades):
    for i_semana in range(semanas):
        suma_temperaturas = 0
        for i_dia in range(len(dias_semana)):
            suma_temperaturas += temperaturas[i_ciudad][i_semana][i_dia]
        promedio = suma_temperaturas / len(dias_semana)
        print(f"Promedio de temperaturas en {ciudad}, Semana {i_semana + 1}: {promedio:.2f}°C")

