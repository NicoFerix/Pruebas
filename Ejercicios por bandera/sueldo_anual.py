# 5.9) El usuario ingresa 12 valores, de a uno por vez, pertenecientes a sus sueldos 
# mensuales durante un año. La computadora muestra su sueldo anual. Si durante la 
# carga de los sueldos mensuales se detecta un valor negativo, esto indica que aún no 
# se ha cobrado el mes en curso, por lo tanto, deben dejar de ingresarse datos y la 
# computadora debe mostrar la sumatoria de sueldos que se llevan cobrados.

sueldosMensuales = 12
sueldoAnual = 0


for sueldos in range(sueldosMensuales):
    sueldoMes = int(input(f"Ingrese el sueldo del {sueldos + 1}° mes: "))

    if sueldoMes > -1 :
        sueldoAnual += sueldoMes

    else:
        print("Aún no se ha cobrado el mes en curso")
        break

print("Sus sueldos cobrados hasta ahora hacen un total de: $",sueldoAnual)

