promedio=float(input("Ingresa tu promedio:"))
if promedio < 0:
    print("Ese promedio no es valido")
elif promedio<=5:
    print("Tu promrdio es muy bajo")
elif promedio>=6 and promedio<=7:
    print("Tu promedio es bajo")
elif promedio>=7 and promedio<=9:
    print("Tu promedio es normal")
elif promedio>9 and promedio<=10:
    print("Tu promedio es excelente")
else:
    print("No seas un hijo del Six Seven ese promedio no existe")