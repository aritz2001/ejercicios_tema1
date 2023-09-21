palabra = input("Ingrese una palabra palindroma: ")

for i in range(len(palabra)-1, -1, -1):
    if palabra[i]!= palabra[len(palabra)-1-i]:
        print("No es palindromo")
        break
    else:
        print("Es palindromo")
        break 