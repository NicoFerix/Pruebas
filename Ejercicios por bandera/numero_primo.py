# 5.10) El usuario ingresa un número entero mayor que 1. Si el número ingresado es 
# incorrecto, volver a pedírselo. La computadora indica si el número ingresado es primo 
# o no.


################### OPCION 1 ###################

continuar = True

while continuar:
    numNatural = int(input("Ingrese un número natural mayor a 1: "))
    
    if numNatural > 1:
        modulo = 2
        primo = True

        while modulo < numNatural:
            if (numNatural % modulo) == 0:
                primo = False
                break
            modulo += 1

        if primo:
            print("El número es un NUMERO PRIMO")
            continuar = False
        else:
            print("El número NO es un NUMERO PRIMO")

    else:
        print("ERROR - El numero ingresado NO ES MAYOR QUE 1")




################### OPCION 2 ###################

# continuar = True

# while continuar:
#     numNatural = int(input("Ingrese un número natural mayor a 1: "))
    
#     if numNatural > 1:
#         modulo = 1
#         cantDivisores = 0

#         while modulo <= numNatural:
#             if (numNatural % modulo) == 0:
#                 cantDivisores += 1
#             modulo += 1

#         if cantDivisores == 2:
#             print("El número es un NUMERO PRIMO")
#             continuar = False
#         else:
#             print("El número NO es un NUMERO PRIMO")

#     else:
#         print("ERROR - El numero ingresado NO ES MAYOR QUE 1")

