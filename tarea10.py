inicio = int(input("Ingresa el número de inicio (por defecto es 100): "))
fin = int(input("Ingresa el número final (por defecto es 0): "))

for i in range(inicio, fin - 1, -1):
    print(i)
