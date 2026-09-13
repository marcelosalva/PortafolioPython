"""Cronómetro de consola con pausas y registro de vueltas."""

# time permite medir el tiempo transcurrido.
import time


def formatear_tiempo(segundos):
    """Convierte segundos en un texto con horas, minutos y segundos."""

    # Convertimos a centésimas: una centésima es 0.01 segundos.
    total_centesimas = int(segundos * 100)

    # divmod devuelve el cociente y el resto de una división.
    horas, resto = divmod(total_centesimas, 360000)
    minutos, resto = divmod(resto, 6000)
    segundos_enteros, centesimas = divmod(resto, 100)

    # :02d muestra al menos dos dígitos, agregando un cero si hace falta.
    return (
        f"{horas:02d}:{minutos:02d}:"
        f"{segundos_enteros:02d}.{centesimas:02d}"
    )


def calcular_transcurrido(acumulado, inicio):
    """Calcula el tiempo total sin contar las pausas."""

    # None indica que el cronómetro está detenido.
    if inicio is None:
        return acumulado

    # perf_counter sirve para medir duraciones.
    return acumulado + time.perf_counter() - inicio


def mostrar_vueltas(vueltas):
    """Muestra la duración de cada vuelta y el tiempo acumulado."""

    if not vueltas:
        print("Todavía no registraste vueltas.")
        return

    print("\n--- VUELTAS ---")

    tiempo_anterior = 0.0

    for numero, tiempo_total in enumerate(vueltas, start=1):
        # Una vuelta dura lo transcurrido desde la vuelta anterior.
        duracion = tiempo_total - tiempo_anterior

        print(
            f"Vuelta {numero}: {formatear_tiempo(duracion)}"
            f" | Total: {formatear_tiempo(tiempo_total)}"
        )

        tiempo_anterior = tiempo_total


def mostrar_menu():
    """Muestra las acciones disponibles."""

    print("\n--- CRONÓMETRO ---")
    print("1. Iniciar o continuar")
    print("2. Ver tiempo")
    print("3. Registrar vuelta")
    print("4. Pausar")
    print("5. Ver vueltas")
    print("6. Reiniciar")
    print("7. Salir")


def main():
    """Controla el cronómetro y las opciones del menú."""

    # Guarda el tiempo medido antes de la última pausa.
    acumulado = 0.0

    # Guarda el instante de inicio. None significa que está detenido.
    inicio = None

    # La lista almacena el tiempo total de cada vuelta registrada.
    vueltas = []

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-7): ").strip()

        if opcion == "1":
            if inicio is not None:
                print("El cronómetro ya está funcionando.")
            else:
                inicio = time.perf_counter()
                print("Cronómetro en marcha.")

        elif opcion == "2":
            transcurrido = calcular_transcurrido(acumulado, inicio)

            print(f"Tiempo: {formatear_tiempo(transcurrido)}")

            if inicio is None:
                print("Estado: detenido.")
            else:
                print("Estado: en marcha.")

        elif opcion == "3":
            if inicio is None:
                print("Primero inicia o continúa el cronómetro.")
                continue

            transcurrido = calcular_transcurrido(acumulado, inicio)

            # La primera vuelta comienza en cero.
            if vueltas:
                tiempo_anterior = vueltas[-1]
            else:
                tiempo_anterior = 0.0

            duracion = transcurrido - tiempo_anterior

            # append agrega una nueva vuelta al final de la lista.
            vueltas.append(transcurrido)

            print(
                f"Vuelta {len(vueltas)}: "
                f"{formatear_tiempo(duracion)}"
            )

        elif opcion == "4":
            if inicio is None:
                print("El cronómetro ya está detenido.")
            else:
                # Guardamos el tiempo antes de marcarlo como detenido.
                acumulado = calcular_transcurrido(acumulado, inicio)
                inicio = None

                print(
                    f"Cronómetro pausado en "
                    f"{formatear_tiempo(acumulado)}"
                )

        elif opcion == "5":
            mostrar_vueltas(vueltas)

        elif opcion == "6":
            confirmacion = input(
                "¿Borrar el tiempo y las vueltas? (s/n): "
            ).strip().lower()

            if confirmacion == "s":
                acumulado = 0.0
                inicio = None

                # clear vacía la lista.
                vueltas.clear()

                print("Cronómetro reiniciado y detenido.")
            else:
                print("Reinicio cancelado.")

        elif opcion == "7":
            transcurrido = calcular_transcurrido(acumulado, inicio)

            print(f"Tiempo final: {formatear_tiempo(transcurrido)}")
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Elige un número del 1 al 7.")


# Inicia el programa cuando ejecutamos este archivo directamente.
if __name__ == "__main__":
    main()