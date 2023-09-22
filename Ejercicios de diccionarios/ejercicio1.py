divisa = {'Euro':'€', 'Dollar':'$','Yen':'��'}
solicitud = input("Ingrese su divisa: ")
if solicitud.title() in divisa:
    print(divisa[solicitud.title()])
else:
    print("Divisa incorrecta")