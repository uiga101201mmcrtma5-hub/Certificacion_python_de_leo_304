c1='Hola'
c2='Mundo'
m="""Esto es una cadena
de varias variables"""
print(c1+c2+m)
#Cadenas y repeticion
e='ja'*3
print(e)
#Cambiar una cadena de mayusculas a minusculas
n='leo'
print(n.upper())
#Cambiar una cadena de minusculas a mayusculas
print(n.lower())
#Remplazar un texto de una cadena
f='me gusta la programacion'
print(f.replace('programacion','matematicas'))
#formato de cadena
ed=16
name='leonel'
dm=f"Hola, me llamo {name}\n y tengo {ed} años"
print(dm)
t='¡Felicidades por aun continuar en el CECY!!!'
cc=len(t)
print(cc)
o='Aprender python es muy divertido'
if 'java' in o:
    print("Encontrado")
else:
 print("no esta")
nl='37'
print(nl.isalpha())
print(nl.isdigit())