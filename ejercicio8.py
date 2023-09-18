numeroenteros = int(input("Ingrese el numero de enteros: "))
espacio = ""
for i in range(1, numeroenteros+1,2):
    for j in range(i,0,-2):
            print(j, end=" ")
    print("")