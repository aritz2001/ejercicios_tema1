lista1 = [1,2,3]
lista2 = [-1,0,2]

lista3 = []
for i,k in zip(lista1,lista2):
    lista3.append(i+k)
print(lista3)