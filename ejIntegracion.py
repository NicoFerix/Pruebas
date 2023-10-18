# Pablo creo un registro de tareas a realizar durante el fin de semana.
# En su registro del dia domingo, tiene anotado que debe ir al supermercado,
# luego lavar el auto, y luego estudiar para un examen. Aunque Pablo ya tiene su
# registro para ese dia, se adelanto y lavo su auto el sabado, para que en su lugar
# pueda ir de picnic con sus hermanos, y pueda, luego de estudiar, ir a cenar con
# sus amigos. Representa tal situacion con un algoritmo desarrollado en python,
# que haga las modificaciones en el registro de pablo y luego muestre el registro
# con este formato.

# #registro original
# tareasDomingo = ["ir al super","lavar el auto","estudiar para el examen"]

# #modificaciones del dia sabado

# tareasDomingo[1] = "ir de picnic con mis hermanos" #actualizando por indice

# tareasDomingo.append("cenar con amigos") #añadimos el dato al final de la lista

# #print(tareasDomingo)

# print("---TAREAS DE DOMINGO----")

# # for numeroTarea in range(len(tareasDomingo)):
# #     print(f"- {tareasDomingo[numeroTarea]}")

# for tarea in tareasDomingo: #ir al super
#     print(f"- {tarea}")

# Observa la imagen.
# Desarrolla un programa que
# solicite al usuario un número del
# 1 al 5 y, en función de ese
# número, determine e imprima el
# nombre del dedo de la mano
# correspondiente, utilizando un
# arreglo con los nombres de los
# dedos.

#datos: tupla nombreDedos  -- numeroDedoIngresado integer

# nombreDedos = ("pulgar","indice","corazon", "anular","meñique")

# numeroDedoIngresado = int(input("Ingrese el numero de dedo para conocer su nombre: "))

# if numeroDedoIngresado < 6 and numeroDedoIngresado > 0:
#     #decir el nombre del dedo
#     print(f"El dedo se llama {nombreDedos[numeroDedoIngresado-1]}")
# else:
#     #dato ingresado no es valido no correponde a un dedo de la mano
#     print("El dato ingresado no es valido no correponde a un dedo de la mano")

# match numeroDedoIngresado:
#     case 1:
#         print(f"El dedo se llama {nombreDedos[0]}")
#     case 2:
#         print(f"El dedo se llama {nombreDedos[1]}")
#     case 3:
#         print(f"El dedo se llama {nombreDedos[2]}")
#     case 4:
#         print(f"El dedo se llama {nombreDedos[3]}")
#     case 5:
#         print(f"El dedo se llama {nombreDedos[4]}")
#     case _:
#         print("El dato ingresado no es valido no correponde a un dedo de la mano")


# Estás desarrollando un programa para una aplicación de
# navegación y necesitas representar los puntos cardinales y sus
# correspondientes grados en un círculo de brújula. Crea un
# registro que contenga los puntos cardinales (Norte, Sur, Este,
# Oeste) y sus respectivos grados (0, 180, 90, 270) en un círculo
# de brújula. Al iniciar el programa debera mostrar la informacion
# con el siguiente formato "En tu brujula encontraras..."
# seguido de
# "El <<puntoCardinal>> a <<grados>> grados ."

#datos : brujula diccionario


# brujula = {
#     # puntoCardinal : grados
#     "Norte" : 0 ,
#     "Sur" : 180 ,
#     "Este" : 90 ,
#     "Oeste" : 270
# }

# print("En tu brujula encontraras...")

# for puntoCardinal, grados in brujula.items():
#     print(f"El {puntoCardinal} a {grados} grados .")

# Desarrolla un programa que gestione una agenda
# telefonica. El programa debe permitir al usuario
# realizar las siguientes acciones: 1->agregar un
# numero de telefono con el nombre del contacto,
# 2->buscar un numero por el nombre y 3->mostrar la
# lista de contactos. El programa finaliza cuando se
# ingrese un 0.

#datos: agendaTelefonica diccionario --- numeroTelefono str -- nombre str -- opcionSeleccionada int

agendaTelefonica = {
    # nombre : numeroTelefono
}

while True:
    opcionSeleccionada = int(input("""
    --AGENDA TELEFONICA MENU DE OPCIONES--
    INGRESE LA OPCION QUE CORRESPONDA
    1 - Agregar contacto a la agenda
    2 - Buscar telefono por nombre
    3 - Ver todos los contactos
    0 - Salir 
    ¿Que desea hacer? """))
    
    match opcionSeleccionada:
        case 0 :
            print("Finalizando el programa. Adios..")
            break 
        case 1:
            #agregar contacto
            nombre = input("Nombre: ")
            numeroTelefono = input("Telefono:")
            #agregamos el par neuvo a la agenda
            
            # nombre : numeroTelefono
            agendaTelefonica[nombre] = numeroTelefono
            
            print("Contacto añadido con exito...")
            
        case 2:
            #buscar por nombre
            nombre = input("Nombre: ")
            telefonoEncontrado = agendaTelefonica.get(nombre , "ERROR - Nombre inexistente")
            print(f"El numero asociado a {nombre} es {telefonoEncontrado}")
        case 3:
            #ver todos los contactos
            for nombre, telefono in agendaTelefonica.items():
                print(f"Nombre contacto: {nombre} . Numero telefono: {telefono}")
        case _:
            print("ERROR- Opcion invalida, intente nuevamente")
