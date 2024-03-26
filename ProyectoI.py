#lista de estudiantes
estudiantes1 = []
print("PROYECTO 1. APRENDIZAJE PHYTON")

while True:

    print("Menu Principal:")
    print("1- Listado de estudiantes")
    print("2- Registrar estudiante")
    print("3- Actualizar Notas del Estudiante")
    print("4- Actualizar Datos del Estudiante")
    print("5- Eliminar estudiante")
    print("6- Salir")
    opcion = input("Elija una opcion: ")
    # Listado de estudiantes
    if opcion == "1":
        print("Listado de estudiantes:")
        if estudiantes1:
            for estudiante in estudiantes1:
                print("Nombre:",estudiante['nombre'])
                print("Apellido:",estudiante['apellido'])
                print("Cedula:", estudiante['cedula'])
                print("Nota 1:", estudiante['nota1'])
                print("Nota 2:", estudiante['nota2'])
                print("Nota 3:", estudiante['nota3'])
                print("Promedio:",estudiante['promedio'])
                print()
        else:
            print("-------------------------------------------")
            print("No hay estudiantes registrados.")
            print("-------------------------------------------")
    # Registrar estudiante
    elif opcion == "2":
        nombre = input("Ingrese el nombre del estudiante: ")
        apellido = input("Ingrese el apellido del estudiante: ")
        cedula = input("Ingrese la cédula del estudiante: ")
        while True:
            nota = input("Ingrese la nota 1: ")
            if nota.isdigit():
                nota1 = float(nota)
                break
            else:
                print("Por favor, ingrese solo números para la nota 1.")
        while True:
            nota = input("Ingrese la nota 2: ")
            if nota.isdigit():
                nota2 = float(nota)
                break
            else:
                print("Por favor, ingrese solo números para la nota 2.")
        while True:
            nota = input("Ingrese la nota 3: ")
            if nota.isdigit():
                nota3 = float(nota)
                break
            else:
                print("Por favor, ingrese solo números para la nota 3.")

        promedio= (nota1+nota2+nota3) / 3
        estudiantes1.append({'nombre': nombre, 'apellido': apellido, 'cedula': cedula, 'nota1': nota1, 'nota2': nota2, 'nota3': nota3, 'promedio': promedio})
        print("-------------------------------------------")
        print("REGISTRO EXITOSO")
        print("-------------------------------------------")
#......# Actualizar Notas del estudiante
    elif opcion == "3":
        cedula = input("Ingrese la cedula del estudiante que desea actualizar: ")
        existe = False
        for estudiante in estudiantes1:
            if estudiante['cedula'] == cedula:
                existe = True
                while True:
                    nota = input("Ingrese la nota 1: ")
                    if nota.isdigit():
                        nota1 = float(nota)
                        break
                    else:
                        print("Por favor, ingrese solo números para la nota 1.")
                while True: 
                    nota=input("Ingrese la nota 2: ")
                    if nota.isdigit():
                        nota2=float(nota)
                        break
                    else: 
                        print('Por favor, ingrese solo números para la nota 2.')
                while True: 
                    nota=input("Ingrese la nota 3: ")
                    if nota.isdigit():
                        nota3=float(nota)
                        break
                    else: 
                        print('Por favor, ingrese solo números para la nota 3.')
                print("Estudiante actualizado exitosamente.")
                break
            break
        if not existe:
            print("-------------------------------------------")
            print("Estudiante no encontrado.")
            print("-------------------------------------------")

     # Actualizar datos del estudiante
    elif opcion == "4":
        cedula = input("Ingrese la cedula del estudiante que desea actualizar: ")
        existe = False
        for estudiante in estudiantes1:
            if estudiante['cedula'] == cedula:
                existe = True
                estudiante['cedula'] =input("Ingrese la cedula del estudiante: ")
                estudiante['nombre'] = input("Ingrese el nombre del estudiante: ")
                estudiante['apellido'] = input("Ingrese el apellido del estudiante: ")
                print("Estudiante actualizado exitosamente.")
                break
        if not existe:
            print("-------------------------------------------")
            print("Estudiante no encontrado.")
            print("-------------------------------------------")
    # Eliminar estudiante
    elif opcion == "5":
        cedula = input("Ingrese la cedula del estudiante que desea eliminar: ")
        existe = False
        for estudiante in estudiantes1:
            if estudiante['cedula'] == cedula:
                existe = True
                estudiantes1.remove(estudiante)
                print("Estudiante eliminado exitosamente.")
                break
        if not existe:
            print("-------------------------------------------")
            print("Estudiante no encontrado.")
            print("-------------------------------------------")
    # 
    elif opcion == "6":
        print("Saliendo del programa...")
        print("-------------------------------------------")
        print("----------------------------")
        print("----------------")
        break
#EL PURGATORIO SIGNIFICA BORRAR LAS NOTAS DEL ESTUDIANTE Y DEJARLAS EN 0
    elif opcion == "7":
        cedula = input("Ingrese la cedula del estudiante que desea enviar al purgatorio:")
        existe = False
        for estudiante in estudiantes1:
            if estudiante['cedula'] == cedula:
                existe = True
                estudiante['nota1'] = 0
                estudiante['nota2'] = 0
                estudiante['nota3'] = 0
                estudiante['promedio'] = 0
                print("Estudiante enviado al purgatorio exitosamente")
                print("-------------------------------------------")
                print("-------------------------------------------")
                print("Nombre:", estudiante['nombre'])
                print("Apellido:",estudiante['apellido'])
                print("Cédula:", estudiante['cedula'])
                print("Nota 1:", estudiante['nota1'])
                print("Nota 2:", estudiante['nota2'])
                print("Nota 3:", estudiante['nota3'])
                print("Promedio:", estudiante['promedio'])
                print("-------------------------------------------")
                print("-------------------------------------------")

                break
        if not existe:
            print("Estudiante no encontrado.")
      
      
       # Opción invalida
    else:
        print("XXXXXXXXXXXX-ERROR-XXXXXXXXXXXXXXXXXXXX ")
        print("Opcion invalida. Por favor, ingrese una opcion valida ")
        print("XXXXXXXXXXXX-ERROR-XXXXXXXXXXXXXXXXXXXX ")
        print("")
        print("")
        print("")
    
