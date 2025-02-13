texto = input("Ingresa un texto: ")

# Se divide el texto en palabras utilizando los espacios en blanco como separadores
palabras = texto.split()

# Se obtiene el número de palabras
conteo_palabras = len(palabras)

print("El número de palabras en el texto es:", conteo_palabras)
