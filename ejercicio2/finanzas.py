from ingresos import ingresos 
from egresos import egresos
    ingresos = 0
    egresos = 0
    opcion = 0
while opcion <=3:
    print("Ponga 1 para poner sus ingresos")
    print("Ponga 2 para poner sus egresos")
    print("Ponga 3 para ver datos")
    opcion = int(input(" "))
if opcion==1:
       ingreso = float(input("Escriba la cantidad de dinero por ingresar "))
       ingresos += ingreso
       print(f"Dinero : {ingresos}")
elif opcion == 2:

        var = int(var)
        egreso = int(input("Escriba la cantidad de dinero por egresarr: "))
    egresos += egresos
       print(f"Dinero : {egresos}")
elif opcion == 3:

        

        print(f"sus ingresos son {ingresos}")
        print(f"sus egresos son -{egresos}")

        

    
