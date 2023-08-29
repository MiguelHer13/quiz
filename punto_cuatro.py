Valores = input("Ingrese valores: ")
Lista_valores = [Valores]

for i in range(len(Lista_valores)):
    if type(Lista_valores[i]) == int:
        print("El valor", Lista_valores[i], "corresponde a un valor entero")
    elif type(Lista_valores[i]) == float:
        print("El valor", Lista_valores[i], "corresponde a un valor decimal")
    elif type(Lista_valores[i]) == str:
        print("El valor", Lista_valores[i], "corresponde a un valor en string")
    elif type(Lista_valores[i]) == tuple:
        print("El valor", Lista_valores[i], "corresponde a un valor en tupla")
    elif type(Lista_valores[i]) == list:
        print("El valor", Lista_valores[i], "corresponde a una lista")
    elif type(Lista_valores[i]) == dict:
        print("El valor", Lista_valores[i], "corresponde a un diccionario")
    else:
        print("El valor", Lista_valores[i], "corresponde a otro tipo de valor")
