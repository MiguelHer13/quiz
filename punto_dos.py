Nombre = input("Introduce tu nombre: ")
print("Su nombre es : " + Nombre + "") 


##########

Lista = []
Personas = int(input("¿Que personas desea almacenar en su lista?: "))

for i in range(Personas):
    nombre = input("Nombre: ")
    Lista.append(nombre)
for i in range(Personas):
    print("Su nombre es:", Lista[i])

