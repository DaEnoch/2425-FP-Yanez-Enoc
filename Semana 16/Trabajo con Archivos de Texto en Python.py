#Creo el archivo para escribir las notas
archivo = open("my_notes.txt", "w")

#Escrito algunas notas
archivo.write("Mis notas personales:\n")
archivo.write("1. Me interesa mucho el mundo de la programación, especialmente escribir: print('Hola mundo') \n")
archivo.write("2. Tengo 17 años \n")
archivo.write("3. Me gusta el encebollado \n")

#cierro el archivo
archivo.close()
print("Archivo 'my_notes.txt' \n")

# Lectura del archivo  :0
archivo = open("my_notes.txt", "r")

# Leer las notas del archivo
print("Contenido del archivo:")
print()

linea = archivo.readline()
while linea:
    print(linea.strip())
    linea = archivo.readline()

# Cerrar el archivo después de leer
archivo.close()