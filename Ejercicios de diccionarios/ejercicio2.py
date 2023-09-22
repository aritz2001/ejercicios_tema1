nombre = input("Ingrese el nombre del archivo: ")
edad = int(input("Ingrese la edad del archivo: "))
direccion = input("Ingrese la direccion del archivo: ")
telefono = int(input("Ingrese el teléfono del archivo: "))
persona = {"nombre": nombre, "edad": edad, "direccion": direccion, "telefono": telefono}
print("el nombre de la persona es: ", persona["nombre"],"su edad es: ", persona["edad"],"su direccion es: ", persona["direccion"],"y su teléfono es: ", persona["telefono"])