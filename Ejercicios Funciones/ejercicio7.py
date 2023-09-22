import math 

def function(x):
    array2 = []
    for i in x:
        cuadrado = i**2
        array2.append(cuadrado)
    return array2



array = [1,2,3,4,5]
function(array)

print(f"La raices cuadradas del array es:{function(array)}")