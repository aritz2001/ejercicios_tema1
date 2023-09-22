import math
def calcular(x,y,z):
    resultadoCirculo = math.pi * x**2
    resultadoCilindro = math.pi * y**3 * z 
    print("El resultado del area del circulo es: ", resultadoCirculo)
    print("El resultado del area del cilindro es: ", resultadoCilindro)



area = int(input("Ingrese el radio del circulo: "))
area2 = int(input("Ingrese el radio del cilindro: "))
altura = int(input("Ingrese la altura del cilindro: "))

calcular(area,area2,altura)