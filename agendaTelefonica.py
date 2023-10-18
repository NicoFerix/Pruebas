# Desarrolla un programa que gestione una agenda telefonica. 
# El programa debe permitir al usuario realizar las siguientes acciones: 
# 1-> Agregar unnumero de telefono con el nombre del contacto.
# 2-> Buscar un numero por el nombre.
# 3-> Mostrar la lista de contactos. 
# 4-> El programa finaliza cuando se ingrese un 0.


agendaContactos = {
    # nombre : numero
}

while True:
    seleccionIngresada = int(input("""
    MENÚ DE AGENDA TELEFÓNICA
    1 - Agendar un nuevo contacto
    2 - Buscar un contacto por su nombre
    3 - Mostrar contactos
    0 - Salir
    ¿QUÉ DESEA HACER? """))

    match seleccionIngresada:
        case 0:
            print("Saliendo del programa. Adiós...")
            break

        case 1:
            # Pido clave y valor
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el teléfono del contacto: ")

            # Ingreso la clave y el valor al dict
            agendaContactos[nombre] = telefono

            print("Contacto añadido correctamente.")

        case 2:
           print(agendaContactos.get(input("Ingrese el nombre del contacto: "), "ERROR - Nombre inexistente."))

        case 3:
            for nombre, telefono in agendaContactos.items():
                print(f"NOMBRE: {nombre} -- TELEFONO: {telefono}")
 
        case _:
            print("ERROR - Opción Incorrecta. Intente nuevamente")

# hola


# COMENTAR UNA PAVADA
# que onda koquito