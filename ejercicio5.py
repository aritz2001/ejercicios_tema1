capital = int(input("Ingrese el capital: "))
interes = float(input("Ingrese el interes: "))
tiempo = int(input("Ingrese el tiempo: "))

for i in range(tiempo):
    if interes > 1:
        capital *= (1 + interes/100)
        print(capital)