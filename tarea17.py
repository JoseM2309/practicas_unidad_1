texto = input("Ingresa un texto: ")

# Eliminar los espacios del texto
texto_sin_espacios = texto.replace(" ", "")

# Contar la cantidad de letras
conteo_letras = len(texto_sin_espacios)

print("El número de letras en el texto es:", conteo_letras)
