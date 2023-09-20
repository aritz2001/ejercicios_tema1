lista = ["Matematica", "Fisica", "Historia", "Lengua"]
repetir = []
for i in lista:
    nota = float(input(f"Que nota has sacado en {i}? "))
    if nota < 5.0:
        repetir.append(i)
        #repetir = print(f"En la asignatura {i} con la nota de {nota} tiene que repetir")
    else:
        continue
for i in repetir:
    lista.remove(i)

print(f"Tienes que repetir:{repetir}")