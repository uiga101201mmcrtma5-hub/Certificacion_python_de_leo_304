p={
    "Nombre":"Leo",
    "Edad":15,
    "Profesion":"Estudiante",
    "Estudiante":False
}
print(p)
print(p["Nombre"])
print(p.get("Edad"))
p["Nombre"]="leo"
print(p["Nombre"])
p["Donde vivo"]="abajo de un puente"
print(p)