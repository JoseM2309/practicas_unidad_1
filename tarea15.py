inicio = int(input("Ingresa el número de inicio (por defecto es 0): "))
fin = int(input("Ingresa el número final (por defecto es 1000): "))

for i in range(inicio, fin + 1):
    if i % 2 == 0:
        print(f"{i} es par")
    else:
        print(f"{i} es impar")
