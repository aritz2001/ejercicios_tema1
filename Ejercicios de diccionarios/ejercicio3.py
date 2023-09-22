frutas = {"platano":1.35,"manzana":0.80,"pera":0.85,"naranja":0.70}
seleccion = input("Ingrese una fruta: ")
kilos = input("Ingrese un numero de kilos: ")
if seleccion in frutas:
    valorfinal = frutas[seleccion] * float(kilos)
    print(f"El precio de la fruta seleccionada es",valorfinal,"€")