palabra = input("Ingrese una palabra: ")
vocales = ["a", "e", "i", "o", "u"]
cantidades = 0
for i in palabra:
    if i in vocales:
        cantidades = cantidades + 1

print(cantidades)