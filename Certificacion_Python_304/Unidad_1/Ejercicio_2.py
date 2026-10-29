try:
    Alumnos=["Emily","Carlos","America","Casillas","Kimberly"]
    Calificaciones=[6.7, 7.5, 9.0, 10, 9.3]
    print("La alumna:",Alumnos[0],"obtuvo una calificacion de:",Calificaciones[0])
    print("La alumna:",Alumnos[1],"obtuvo una calificacion de:",Calificaciones[1])
    print("La alumna:",Alumnos[2],"obtuvo una calificacion de:",Calificaciones[2])
    print("La alumna:",Alumnos[3],"obtuvo una calificacion de:",Calificaciones[3])
    print("La alumna:",Alumnos[4],"obtuvo una calificacion de:",Calificaciones[4])
except IndexError:
    print("ese indice no existe")