#Ciclo externo para el numero de la base de la tabla
for i in range(1,4):
    print(f"---Tabla del {i}---")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print(f"!Aque termina la tabla del {i}")