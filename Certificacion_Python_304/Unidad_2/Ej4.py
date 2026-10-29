Mapa = [
    [".",".",".",".",],
    [".",".","X",".",],
    [".",".",".","."],
    [".",".",".",".",]
]
f = len(Mapa)
c = len(Mapa)
#Recorriendo las materias
#Ciclo para manejar filas
for i in range(f):
    #Ciclo externo para los indices de las filas
    for j in range(c):
        #verificamos si encontramos el tesoro
        if Mapa [i][j]=="X":
            print(f"Mapa encontrado eb la posicion [{i}],[{j}]")
            print(f"Mapa encontrado eb la posicion [{i}],[{j}]")
            print(f"Mapa encontrado eb la posicion [{i}],[{j}]")
            