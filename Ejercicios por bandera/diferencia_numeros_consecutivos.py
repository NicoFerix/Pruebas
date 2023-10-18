#5.4) Se ingresan números hasta que la diferencia entre dos números consecutivos se repita. La computadora muestra la cantidad de números ingresados.

diferencia = 0
diferenciaGuardada = 0
numeroGuardado = 0
contador = 0
Salida = True

while Salida:
    
    numeroIngresado = int(input("Ingresar un número hasta que su diferencia se repita con el consecutivo: "))
    diferencia = numeroIngresado - numeroGuardado

    if diferencia == diferenciaGuardada: 
        Salida = False
        
    else:
        diferenciaGuardada = diferencia
        numeroGuardado = numeroIngresado

    
    contador += 1

print(f"La cantidad de números ingresados es: {contador}")


    
    
    











