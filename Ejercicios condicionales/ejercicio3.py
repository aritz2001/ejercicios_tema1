primernumero = int(input("Ingrese el primer numero: "))
segundonumero = int(input("Ingrese el segundo numero: "))
if segundonumero == 0:
    print("error")
else:
    resultado = primernumero / segundonumero
    print(int(resultado))