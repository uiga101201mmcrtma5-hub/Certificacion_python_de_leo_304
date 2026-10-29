#Creando una matriz
n = [
    ["A","B","C","D","E","F","G","H","I","J","K","L","M",],
    ["N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],
]
#Obteniendo el numero de filas
#f=len(n)#filas=3
#Obteniendo el mumero de columnas
#c=len(n[0])
#Ciclo externo para los indices de las filas
for i in range(0,2):
    #Ciclo interno para los indices de las columnas
    for j in range(0,13):
        print(f"[{i}][{j}]={n[i][j]}")