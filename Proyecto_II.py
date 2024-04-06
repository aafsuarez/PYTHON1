from datetime import datetime
#funciones
def menu_principal():
    print("-- MENU PRINCIPAL ---")
    print("1. Lista de tareas")
    print("2. Filtrar Tareas")
    print("3. Añadir Tareas")
    print("4. Actualizar Tareas")
    print("5. Eliminar Tareas")
    print("6. Salir del programa")

def menu_lista():
    print("--- LISTA DE TAREAS ---")
    print("1. Completadas")
    print("2. Pendientes")
    print("3. Atras")

def menu_filtrado():
    print("--- FILTRAR TAREAS ---")
    print("1. Por codigo")
    print("2. Por titulo")
    print("3. Por fecha")
    print("4. Atras")

def menu_actualizar():
    print("-- ACTUALIZAR TAREAS ---")
    print("1. Actualizar Codigo")
    print("2. Actualizar Titulo")
    print("3. Actualizar Descripcion")
    print("4. Actualizar Estatus")
    print("5. Actualizar Fecha")
    print("6. Atras")

def menu_eliminar():
    print("--- ELIMINAR TAREAS ---")
    print("1. Por código")
    print("2. Atrás")

def agregar_tarea(tareas):
    codigo = input("Ingrese el codigo de la tarea: ")
    
    codigos_existentes = [tarea['codigo'] for tarea in tareas]
    while codigo in codigos_existentes:
        print("El codigo ya existe. Intente con un codigo diferente.")
        codigo = input("Ingrese el codigo de la tarea: ")


    titulo = input("Ingrese el titulo de la tarea: ")
    descripcion = input("Ingrese la descripcion de la tarea: ")   
#fecha 
    while True:
        fecha= input("Ingrese la fecha de la tarea (Formato: DD-MM-YYYY): ")
        try:
            fecha = datetime.strptime(fecha, "%d-%m-%Y").date()
            break
        except ValueError:
            print("Formato de fecha incorrecto. Intente nuevamente.")

    while True:
        estado = input("Ingrese el estado de la tarea (Completada C, Pendiente P): ").lower()
        if estado in ['completada', 'c']:
            estado = True
            break
        elif estado in ['pendiente', 'p']:
            estado = False
            break
        else:
            print("Estado no valido. Por favor, ingrese 'Completada' o 'Pendiente'.")
    tarea = {
    'codigo': codigo,
    'titulo': titulo,
    'descripcion': descripcion,
    'fecha': fecha,
    'completada': estado
    }
    tareas.append(tarea)
    print("Tarea añadida exitosamente.")

def mostrar_tareas(tareas,completadas=True):
    print("--- TAREAS {} ---".format("COMPLETADAS" if completadas else "PENDIENTES"))
    for tarea in tareas:
        if tarea['completada'] == completadas:
            estado = "completada" if tarea['completada'] else "Pendiente"
            print(f"Codigo:{tarea['codigo']},titulo: {tarea['titulo']},Estado:{estado},Fecha: {tarea['fecha']}")
    print("")

def filtrar_porcodigo(tarea, codigo):
    return codigo in tarea['codigo']

def filtrar_portitulo(tarea, titulo):
    return tarea['titulo'].lower().find(titulo.lower()) !=-1

def filtrar_porfecha(tarea, fecha):
    return tarea['fecha'] == fecha

def mostrar_tareasfiltradas(tareas_filtradas):
    if not tareas_filtradas:
        print("No se encontraron tareas que coincidan con el filtro.")
    else:
        for tarea in tareas_filtradas:
            print(f"Código: {tarea['codigo']}, Título: {tarea['titulo']}, Fecha: {tarea['fecha']}")

def eliminar_tarea(tareas, codigo):
    tarea_encontrada = False
    for tarea in tareas:
        if tarea['codigo'] == codigo:
            tareas.remove(tarea)
            tarea_encontrada = True
            print("Tarea eliminada exitosamente.")
            break
    if not tarea_encontrada:
        print("El codigo proporcionado no corresponde a ninguna tarea.")

def actualizar_tarea(tareas, codigo, opcion_actualizacion):
    tarea_encontrada = False
    for tarea in tareas:
        if tarea['codigo'] == codigo:
            tarea_encontrada = True
            if opcion_actualizacion == '1':
                nuevo_codigo = input("Ingrese el nuevo codigo de la tarea: ")
                tarea['codigo'] = nuevo_codigo
            elif opcion_actualizacion == '2':
                nuevo_titulo = input("Ingrese el nuevo titulo de la tarea: ")
                tarea['titulo'] = nuevo_titulo
            elif opcion_actualizacion == '3':
                nueva_descripcion = input("Ingrese la nueva descripcion de la tarea: ")
                tarea['descripcion'] = nueva_descripcion
            elif opcion_actualizacion == '4':
                nuevo_estado = input("Ingrese el nuevo estado de la tarea (Completada C, Pendiente P): ").lower()
                if nuevo_estado in ['completada', 'c']:
                    tarea['completada'] = True
                elif nuevo_estado in ['pendiente', 'p']:
                    tarea['completada'] = False
                else:
                    print("Estado no válido.")
            elif opcion_actualizacion == '5':
                while True:
                    nueva_fecha_str = input("Ingrese la nueva fech de la tarea (Formato: DD-MM-YYYY): ")
                    try:
                        nueva_fecha = datetime.strptime(nueva_fecha_str, "%d-%m-%Y").date()
                        tarea['fecha'] = nueva_fecha
                        break
                    except ValueError:
                        print("Formato de fecha incorrecto. Intente nuevamente.")
            else:
                print("Opción de actualización no válida.")
            print("Tarea actualizada exitosamente.")
            break

    if not tarea_encontrada:
        print("El código proporcionado no corresponde a ninguna tarea.")
              
#funcion principal
def main():
    tareas = [] 
    while True:
        menu_principal()
        opcion = input("Selecciona una opcion: ")

        if opcion == '1':
            while True:
                menu_lista()
                lista_opcion = input("Selecciona una opcion de la lista de tareas: ")

                
                if lista_opcion == '1':
                    mostrar_tareas(tareas, completadas=True)
                elif lista_opcion == '2':
                    mostrar_tareas(tareas, completadas=False)
                elif lista_opcion == '3':
                    break
                else:
                    print("Opcion no valida. Intentalo de nuevo.")
#Menu Filtrado
        elif opcion == '2':
            while True:
                menu_filtrado()
                filtrado_opcion = input("selecciona una opcion:  ")

                if filtrado_opcion=='1':
                    for tarea in tareas:
                        print(f"Código: {tarea['codigo']}, Título: {tarea['titulo']}")
                        print('--------------------------------------------------')
                        print('--------------------------------------------------')

                    codigo=input("Ingrese el codigo para filtrar:  ")
                    tareas_filtradas=filter(lambda tarea:filtrar_porcodigo(tarea,codigo),tareas)
                    mostrar_tareasfiltradas(list(tareas_filtradas))

                elif filtrado_opcion == '2':
                    for tarea in tareas:
                        print(f"Código: {tarea['codigo']}, Título: {tarea['titulo']}, Fecha: {tarea['fecha']}")
                        print('-----------------------------------------------------------')
                        print('-----------------------------------------------------------')
                    titulo = input("Ingrese el titulo para filtrar:  ")
                    tareas_filtradas = filter(lambda tarea: filtrar_portitulo(tarea, titulo), tareas)
                    mostrar_tareasfiltradas(list(tareas_filtradas))
                    
                elif filtrado_opcion == '3':
                    for tarea in tareas:
                        print(f"Código: {tarea['codigo']}, Título: {tarea['titulo']}, Fecha: {tarea['fecha']}")
                        print('-----------------------------------------------------------')
                        print('-----------------------------------------------------------')

                    while True:
                        fecha_str = input("Ingrese la fecha para filtrar tareas (Formato: DD-MM-YYYY): ")
                        try:
                            fecha = datetime.strptime(fecha_str, "%d-%m-%Y").date()
                            tareas_filtradas = filter(lambda tarea: filtrar_porfecha(tarea, fecha), tareas)
                            mostrar_tareasfiltradas(list(tareas_filtradas))
                            break
                        except ValueError:
                             print("Formato de fecha incorrecto. Intente nuevamente.")
                elif filtrado_opcion == '4':
                    break
    
                else:
                    print("Opcion no valida. Intenta nuevamnte ")
#Menu Agregar 
        elif opcion == '3':
            agregar_tarea(tareas)           
#Menu Actualizar 
        elif opcion == '4':
            while True:
                menu_actualizar()
                Actualizar_opcion = input("Selecciona una opcion para actualizar tareas: ")
                if Actualizar_opcion in ['1', '2', '3', '4', '5']:
                    codigo = input("Ingrese el cdigo de la tarea que desea actualizar: ")
                    actualizar_tarea(tareas, codigo, Actualizar_opcion)
                elif Actualizar_opcion == '6':
                    break
                else:
                    print("Opcion no valida. Intentalo de nuevo.")
#Menu Eliminar 
        elif opcion == '5':
            menu_eliminar()
            opcion_eliminar=input("Seleccione una opcion: ")
            while True: 
                if opcion_eliminar == '1':
                    codigo = input("Ingrese el código de la tarea que desea eliminar: ")
                    eliminar_tarea(tareas, codigo)
                elif opcion_eliminar == '2':
                    return
                else:
                    print("Opción no válida. Inténtalo de nuevo.")
#Salir
        elif opcion == '6':
            print("Saliendo del programa...")
            break

        else:
            print("Opcion no valida. Intentalo de nuevo.")

if __name__ == "__main__":
    main()
