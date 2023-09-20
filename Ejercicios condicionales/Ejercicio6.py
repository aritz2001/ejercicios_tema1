nombre = input("Ingrese el nombre del archivo:")
sexo = input("Ingrese el sexo del archivo: ")
grupoa = "M"
grupob = "N"
if sexo == "M": 
    if nombre.lower() < "M":
        print("Eres del grupo A")
    else:
            print("Eres del grupo B")
else:
    if nombre.lower() > "N":
        print("Eres del grupo A")
    else:
        print("Eres del grupo B")
