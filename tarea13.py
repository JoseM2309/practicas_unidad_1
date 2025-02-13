inicio = int(input("Ingresa el número de inicio (por defecto es 1000): "))
fin = int(input("Ingresa el número final (por defecto es 0): "))
paso = 3

for i in range(inicio, fin - 1, -paso):
    print(i)
