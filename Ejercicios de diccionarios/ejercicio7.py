articulos = {}
precio = {}
continuar = True
while continuar:
    ingresarArticulo = input("Ingrese el nombre del articulo: ")
    articulos = [ingresarArticulo] 
    ingresarPrecio = input("Ingrese el precio del articulo: ")
    precio = [ingresarPrecio]
    continuar = input("Desea agregar otro articulo? (S/N): ")
    if continuar == "S" or continuar == "s" :
        continuar = True
    else:
        continuar = False
total = sum(precio.values())
print("Los articulos ingresados son: ",articulos,"\nLos precios de dichos articulos son: ",precio,"\n y el precio totales es:",total)


