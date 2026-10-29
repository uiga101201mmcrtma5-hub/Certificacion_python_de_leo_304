try:
    materias=["Programacion","Filosofia","Matematicas","Igles"]
    print(materias[2])
    materias.append("Lengua y Comunicacion")
    print(materias)
    materias[1]="Biologia"
    print(materias)
    materias.remove("Matematicas")
    print(materias)
except IndexError:
    print("ese indice no existe")