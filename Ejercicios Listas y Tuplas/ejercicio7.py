abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
abecedarios = len(abecedario) - int(len(abecedario) / 3)
for i in range(0,abecedarios):
    if i%3 == 0: 
        abecedario.remove(abecedario[i])
    print(abecedario)