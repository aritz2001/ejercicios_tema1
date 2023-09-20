edad = int(input("Ingrese su edad: "))
ingresosanuales = int(input("Ingrese su ingresos anuales: "))
ingresosamensuales = ingresosanuales / 12

if edad >= 16 and ingresosamensuales >= 1000:
    print("Tienes que tributar")
else:
    print("No tienes que tributar")
