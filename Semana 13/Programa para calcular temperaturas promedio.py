def calcular_temperatura_promedio(datos_ciudades):

    promedios = {}

    for ciudad, temperaturas in datos_ciudades.items():
        #promedio de las temperaturas
        promedio = sum(temperaturas) / len(temperaturas)
        promedios[ciudad] = promedio

    return promedios

datos_ciudades = {
    "Quito": [18, 19, 20, 18],  #temperaturas de quito
    "Manta": [28, 30, 29, 27],  #temperaturas de manta
    "Tena": [22, 24, 25, 28]  #temperaturas de tena
}

resultados = calcular_temperatura_promedio(datos_ciudades)

print("Temperaturas Promedio por Ciudad:")
for ciudad, promedio in resultados.items():
    print(f"{ciudad}: {promedio}°C")

#Eso es todo!! :D