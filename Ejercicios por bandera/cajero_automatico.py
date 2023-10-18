# 5.5) Una cuenta bancaria tiene 30000 pesos de saldo. 
# El usuario ingresará valores que corresponden a extracciones vía cajero automático. 
# Por cada extracción se debe mostrar como quedó el saldo luego de la operación. 
# Una extracción que supere al saldo disponible se debe rechazar indicando que no es posible la operación.
# El programa finaliza cuando el saldo queda en cero.


cuentaBancaria = 30000
ejecutar = True
extraccion = 0

while ejecutar:

    eleccion = int(input("""
--CAJERO AUTOMÁTICO--
¿Desea retirar dinero?
1 - Si.
2 - No. 
>: """))

    if eleccion == 1:

        extraccion = int(input(f"""
Usted dispone de: ${cuentaBancaria}
¿Cuánto dinero desea retirar?
>: """))

        if cuentaBancaria >= extraccion:
            cuentaBancaria -= extraccion
            print(f"Su fondo es: {cuentaBancaria}")
        else:
            print("ERROR - El monto ingresado supera al saldo disponible.")
        
        if cuentaBancaria == 0:
            print("""
Se ha quedado sin fondos. 
Saliendo del programa. 
      Adiós...""")
            ejecutar = False

    elif eleccion == 2:
        print("Saliendo del programa. Adiós...")
        ejecutar = False

    else:
        print("ERROR - Opción Incorrecta - Intente nuevamente")