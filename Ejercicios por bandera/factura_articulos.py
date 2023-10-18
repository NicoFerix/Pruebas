# 5.7) Desarrollar un programa que pida una cantidad de artículos comprados y el 
# precio unitario de ese artículo. Por cada carga debe preguntar si se desea seguir 
# ingresando de la forma “¿Desea ingresar otro artículo? [S/N]”. La carga de datos 
# finaliza cuando se detecta una n o N. La computadora debe mostrar el monto de la factura

precioUnitario = 0
cantArticulos = 0
nvoArticulo = ""
factura = 0
continuar = True

while continuar:

    nvoArticulo = input("¿Desea ingresar un artículo? [S/N] : ")

    if nvoArticulo.lower() == "s":
        cantArticulos = int(input("Ingrese la cantidad de artículos que desea comprar : "))
        precioUnitario = int(input("Ingrese el precio unitario del artículo : "))
        factura += cantArticulos * precioUnitario

    elif nvoArticulo.lower() == "n":
        continuar = False
        
    else:
        print("ERROR - Opción incorrecta. Intente nuevamente")

print(f"El monto total de la factura es : ${factura}")
print("Adiós...")