# 5.8) En un colegio existe la posibilidad de elegir, en la materia "lengua extranjera", 
# entre las siguientes opciones: [I]nglés, [F]rancés, [P]ortugués y [A]lemán. Se ingresa,
# para cada alumno, la lengua elegida. La computadora muestra el porcentaje de 
# alumnos que eligió cada lengua, en forma de número y en forma gráfica (histograma),
# utilizando líneas hechas con asteriscos. 

# Inicializar contadores para cada lengua
contador = 0
ingles = 0
frances = 0
portugues = 0
aleman = 0

# Obtener la cantidad de alumnos
numAlumnos = int(input("Ingrese la cantidad de alumnos inscriptos en 'Lenguas Extranjeras': "))

while contador < numAlumnos:
    
    lengua = input(f"Ingrese la lengua a la que se a inscripto el {contador + 1}° alumno\n ---[I]nglés, [F]rancés, [P]ortugués y [A]lemán---  : ")
    
    match lengua.upper():
        case "I":
            ingles += 1

        case "F":
            frances += 1

        case "P":
            portugues += 1

        case "A":
            aleman += 1

        case _:
            print("ERROR - Opción incorrecta. Intente nuevamente.")
            continue

    contador += 1

# Calcular porcentajes de inscriptos por lengua
porcentajeIngles = ingles / numAlumnos
porcentajeFrances = frances / numAlumnos
porcentajePortugues = portugues / numAlumnos
porcentajeAleman = aleman / numAlumnos

# Mostrar resultados numéricos
print("\n\tPorcentajes:")
print(f"Porcentaje de alumnos inscriptos en Inglés: {porcentajeIngles:.2%}")
print(f"Porcentaje de alumnos inscriptos en Francés: {porcentajeFrances:.2%}")
print(f"Porcentaje de alumnos inscriptos en Portugués: {porcentajePortugues:.2%}")
print(f"Porcentaje de alumnos inscriptos en Alemán: {porcentajeAleman:.2%}")

# Mostrar histograma
print("\n\tHistograma:")
print("Inglés:   ", "*" * int(porcentajeIngles * 100))
print("Francés:  ", "*" * int(porcentajeFrances * 100))
print("Portugués:", "*" * int(porcentajePortugues * 100))
print("Alemán:   ", "*" * int(porcentajeAleman * 100))