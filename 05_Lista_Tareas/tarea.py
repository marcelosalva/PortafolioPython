"""Lista de tareas para consola."""


# Esta lista guardará todas las tareas que agregue el usuario.
tareas = []


def mostrar_menu():
    """Muestra las opciones disponibles del programa."""

    print("\n--- LISTA DE TAREAS ---")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")


def ver_tareas():
    """Muestra todas las tareas guardadas."""

    if not tareas:
        print("No hay tareas guardadas.")
    else:
        print("\nTus tareas:")

        for posicion, tarea in enumerate(tareas, start=1):
            estado = "✅" if tarea["completada"] else "⏳"
            print(f"{posicion}. {estado} {tarea['nombre']}")


def agregar_tarea():
    """Pide una tarea al usuario y la agrega a la lista."""

    nombre = input("Escribe la nueva tarea: ").strip()

    if nombre == "":
        print("La tarea no puede estar vacía.")
    else:
        tarea = {
            "nombre": nombre,
            "completada": False
        }

        tareas.append(tarea)
        print("Tarea agregada correctamente.")


def pedir_posicion():
    """Pide el número de una tarea y valida que exista."""

    while True:
        try:
            posicion = int(input("Escribe el número de la tarea: "))

            if posicion < 1 or posicion > len(tareas):
                print("Ese número de tarea no existe.")
            else:
                return posicion - 1

        except ValueError:
            print("Entrada no válida. Escribe un número entero.")


def completar_tarea():
    """Marca una tarea como completada."""

    if not tareas:
        print("No hay tareas para completar.")
    else:
        ver_tareas()
        posicion = pedir_posicion()

        tareas[posicion]["completada"] = True
        print("Tarea marcada como completada.")


def eliminar_tarea():
    """Elimina una tarea de la lista."""

    if not tareas:
        print("No hay tareas para eliminar.")
    else:
        ver_tareas()
        posicion = pedir_posicion()

        tarea_eliminada = tareas.pop(posicion)
        print(f"Tarea eliminada: {tarea_eliminada['nombre']}")


while True:
    mostrar_menu()

    opcion = input("Elige una opción (1-5): ").strip()

    if opcion == "1":
        ver_tareas()

    elif opcion == "2":
        agregar_tarea()

    elif opcion == "3":
        completar_tarea()

    elif opcion == "4":
        eliminar_tarea()

    elif opcion == "5":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Elige un número del 1 al 5.")