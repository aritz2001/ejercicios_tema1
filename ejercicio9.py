contrasena = input("Ingrese la contraseña: ")
while contrasena != "contraseña":
    print("Ingrese una contraseña válida")
    contrasena = input("Ingrese de nuevo la contraseña: ")
else:
    print("Contraseña correcta")