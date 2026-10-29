try:
   v=int(input("Piensa en un numero:"))
   while v !=  67:
      print("ERROR:Ahora intenta con un  67")
      v=int(input("Ingresalo aqui:"))
   else:
      for i in range(1,68):
         print(i,"Six seven")
except ValueError:
   print("---INGRESA UN MALDITO 67---")
   v=int(input("Piensa en un numero:"))
   while v !=  67:
      print("ERROR:Ahora intenta con un  67")
      v=int(input("Ingresalo aqui:"))
   else:
      for i in range(1,68):
         print(i,"Six seven")