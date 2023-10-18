# 5.6) Desarrollar un programa que pida un carácter al usuario y que por cada carga 
# pregunte si se desea seguir ingresando. 
# De la forma “¿Desea ingresar otro carácter? [S/N]”.
# La carga de datos finaliza cuando se detecta una n o N. 
# La computadora debe mostrar la cantidad de letras vocales ingresadas. 
# (Debe admitir mayúsculas y minúsculas).

continuar = True
cantVocales = 0

while continuar :

    eleccion = input("""
    --CARACTERES--
    ¿Desea ingresar un caracter?
    [s] - Si.
    [n] - No. 
    >: """)

    if eleccion.lower() == "s":
        caracter = input("Ingrese un caracter: ")

        if caracter.lower() in "aeiou":
            cantVocales += 1


    elif eleccion.lower() == "n":
        print("Saliendo del programa...")
        break

    else:
        print("ERROR - La opción ingresada es incorrecta")

print(f"La cantidad de vocales ingresadas fueron: {cantVocales}")
print("Adios...")