numero = int(input('Escribe un numero: '))

def factorial(numero):
    if numero == 0 or numero == 1:
        resultado = 1
    elif numero > 1:
        resultado = numero * factorial(numero - 1)
    return resultado
  


factorial(numero)
fact = factorial(numero)
print("El factorial del numero ingresado es: ", fact)