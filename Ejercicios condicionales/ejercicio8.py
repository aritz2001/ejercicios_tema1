evaluacion = float(input("Ingrese su numero de evaluaciones: "))
salario = int(2400)

if evaluacion == 0.0:
    print("La cantidad de dinero que has conseguido es de", salario)
elif evaluacion == 0.4:
    salarioevaluado = salario * 0.4
    salarioResultante = salario  + salarioevaluado
    print("La cantidad de dinero que has conseguido es de", salarioResultante)
    
elif evaluacion >= 0.6:
    salarioevaluado = salario * 0.6
    salarioResultante = salario  + salarioevaluado
    print("La cantidad de dinero que has conseguido es de", salarioResultante)
else:
    print("Error")