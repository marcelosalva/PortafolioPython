"""Juego de Piedra, Papel o Tijera."""

# random permite que la computadora elija al azar.
import random


def mostrar_menu():
    """Muestra las opciones del juego."""

    print("\n--- PIEDRA, PAPEL O TIJERA ---")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Salir")


def obtener_eleccion_computadora():
    """La computadora elige una opción al azar."""

    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)


def convertir_eleccion(numero):
    """Convierte el número elegido en una palabra."""

    elecciones = {
        "1": "piedra",
        "2": "papel",
        "3": "tijera",
    }

    return elecciones.get(numero)


def determinar_ganador(jugador, computadora):
    """Compara las elecciones y determina el resultado."""

    # Si ambos eligen lo mismo, es un empate.
    if jugador == computadora:
        return "empate"

    # Estas son las combinaciones en las que gana el jugador.
    jugador_gana = (
        (jugador == "piedra" and computadora == "tijera")
        or (jugador == "papel" and computadora == "piedra")
        or (jugador == "tijera" and computadora == "papel")
    )

    if jugador_gana:
        return "jugador"

    return "computadora"


def mostrar_puntuacion(puntos_jugador, puntos_computadora):
    """Muestra los puntos actuales."""

    print("\n--- PUNTUACIÓN ---")
    print(f"Jugador: {puntos_jugador}")
    print(f"Computadora: {puntos_computadora}")


def main():
    """Ejecuta el juego hasta que el usuario decida salir."""

    puntos_jugador = 0
    puntos_computadora = 0

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ").strip()

        if opcion == "4":
            print("¡Gracias por jugar!")
            break

        jugador = convertir_eleccion(opcion)

        # Si la conversión devuelve None, la opción no era válida.
        if jugador is None:
            print("Opción no válida. Elige un número del 1 al 4.")
            continue

        computadora = obtener_eleccion_computadora()

        print(f"\nTú elegiste: {jugador}")
        print(f"La computadora eligió: {computadora}")

        resultado = determinar_ganador(jugador, computadora)

        if resultado == "empate":
            print("¡Es un empate!")

        elif resultado == "jugador":
            print("¡Ganaste esta ronda!")
            puntos_jugador += 1

        else:
            print("La computadora ganó esta ronda.")
            puntos_computadora += 1

        mostrar_puntuacion(puntos_jugador, puntos_computadora)


# Esta condición inicia el programa.
if __name__ == "__main__":
    main()
        