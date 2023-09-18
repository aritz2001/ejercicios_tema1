numeroprimo = input("Ingrese un numero primo: ")

for i in range(2,int(numeroprimo)+1):
    if int(numeroprimo)%i == 0:
        print(f"El numero {numeroprimo} no es primo")
        break
    else:
        print(f"El numero {numeroprimo} es primo")
        break