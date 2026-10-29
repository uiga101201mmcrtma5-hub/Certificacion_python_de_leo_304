#Creando una matriz
n = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#Obteniendo el numero de filas
#f=len(n)#filas=3
#Obteniendo el mumero de columnas
#c=len(n[0])
#Ciclo externo para los indices de las filas
for i in range(0,3):
    #Ciclo interno para los indices de las columnas
    for j in range(0,3):
        print(f"[{i}][{j}]={n[i][j]}")