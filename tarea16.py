nombres = []

# Solicitar 5 nombres
for i in range(5):
    nombre = input(f"Ingrese el nombre {i + 1}: ")
    nombres.append(nombre)

# Ordenar los nombres alfabéticamente
nombres.sort()

# Mostrar la lista de nombres ordenada alfabéticamente
print("\nLos nombres en orden alfabético son:")
print(nombres)

# Iterar del último al primero
print("\nIterando de último al primero:")
for nombre in reversed(nombres):
    print(nombre)
