Materias = ["Calculo", "Ingles", "Programación", "Ecuaciones", "Variable", "Circuitos"]
Nota = []
for conjunto_materias in Materias:
    x = input("¿Qué calificación sacó en la asignatura " + conjunto_materias + "? : ")
    Nota.append(x)

    
for i in range(len(Materias)):
    print("En " + Materias[i] + " su calificación fue de: " + Nota[i])