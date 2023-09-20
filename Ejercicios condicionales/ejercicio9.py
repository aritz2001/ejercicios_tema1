edad = int(input("Ingrese su edad: "))
menor = "gratis"
entre = 5
mayor = 10
if edad < 4:
   print("Tu entras",menor)
elif edad >= 4 and edad < 18:
    print("Tu tienes que pagar",entre,"€")
else:
    print("Tu tienes que pagar",mayor,"€")