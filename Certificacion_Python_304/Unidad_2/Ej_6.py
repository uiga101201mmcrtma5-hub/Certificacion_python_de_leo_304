t= [
    ["Nombre:","Edad","Calificacion"],
    ["Emily",16,6.7],
    ["Carlos Yair",16,8.0],
    ["Leonel",15,6.7],
    ["America",15,10.0],
    ["Luis Michel",16,3.0],
    ["Carlos",16,8.0],
    ["Sdana",16,7.0],
    ["Brian",16,8.0],
    ["Kimberly",16,9.0]
    
]
n = input("Ingresa un nombre:")
f = len(t)
c = len(t[0])
for i in range(f):
    for j in range(c):
            if t[i][j]==n:
                  print(f"Nombre encontrado en la posicion [{i}],[{j}]")
                  print("Nombre", f"[{i}],[{j}]")