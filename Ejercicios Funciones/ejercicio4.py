def funcion(x,y):
    
    if y > 0:
        resultado = x * y
        resu = resultado + x
        print("La cantidad de la factura con IVA es: ", resu) 

    else:
        y = 0.21
        resultado = x * y
        resu = resultado + x
        print("La cantidad de la factura con el IVA es: ", resu)


factura = int(input("Ingrese la cantidad de la factura: "))
iva = float(input("Ingrese el IVA: "))
funcion(factura,iva)