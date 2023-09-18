palabra = input("Ingrese una palabra: ")
letra = input("Ingrese una letra: ")
cantidad = 0
for i in range(len(palabra)):
    if letra == palabra[i]:
        cantidad = cantidad + 1
        print("La letra", letra, "se encuentra en la palabra", palabra, "y se encuentra", cantidad, "veces")
        