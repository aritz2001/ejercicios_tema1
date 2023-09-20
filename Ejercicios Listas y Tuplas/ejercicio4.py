ganadores = []
for i in range(6):
    ganadores.append(int(input(f"Ingrese el numero ganador de la loteria: " )))
ganadores.sort()
print("Los numeros ganadores de la loteria son" + str(ganadores))
