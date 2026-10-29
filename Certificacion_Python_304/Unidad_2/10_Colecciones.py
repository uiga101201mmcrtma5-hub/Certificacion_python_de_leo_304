run_run=[]
n = int(input("Ingresa el numero de productos:"))
for i in range(n):
    p=input("Ingresa el producto a tu run run:")
    run_run.append(p)
print("---Lista creada correctamente---")
run_run[0]="barritas"
print(run_run[0])
print(run_run[1])
print(run_run)