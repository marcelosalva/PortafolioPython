"""Quiz de preguntas sobre Python para consola."""

# random permite cambiar el orden de las preguntas.
import random


# Una lista puede contener varios diccionarios.
# Cada diccionario representa una pregunta del quiz.
PREGUNTAS = [
    {
        "pregunta": "¿Qué función muestra un mensaje en la consola?",
        "opciones": [
            "1. input()",
            "2. print()",
            "3. len()",
        ],
        "correcta": "2",
        "explicacion": "print() muestra información en la consola.",
    },
    {
        "pregunta": "¿Qué función recibe texto del usuario?",
        "opciones": [
            "1. input()",
            "2. print()",
            "3. int()",
        ],
        "correcta": "1",
        "explicacion": "input() recibe lo escrito y devuelve un texto.",
    },
    {
        "pregunta": "¿En qué posición comienza una lista?",
        "opciones": [
            "1. En la posición 1",
            "2. En la posición -1",
            "3. En la posición 0",
        ],
        "correcta": "3",
        "explicacion": "El primer elemento de una lista tiene índice 0.",
    },
    {
        "pregunta": "¿Qué palabra usamos para definir una función?",
        "opciones": [
            "1. def",
            "2. if",
            "3. for",
        ],
        "correcta": "1",
        "explicacion": "def permite definir una función.",
    },
    {
        "pregunta": "¿Qué instrucción termina un bucle?",
        "opciones": [
            "1. continue",
            "2. break",
            "3. input",
        ],
        "correcta": "2",
        "explicacion": "break termina el bucle que lo contiene.",
    },
    {
        "pregunta": "¿Qué método agrega un elemento al final de una lista?",
        "opciones": [
            "1. strip()",
            "2. upper()",
            "3. append()",
        ],
        "correcta": "3",
        "explicacion": "append() agrega un elemento al final de una lista.",
    },
]


def pedir_respuesta():
    """Pide una respuesta hasta recibir una opción válida."""

    while True:
        # strip elimina espacios del principio y del final.
        respuesta = input("Tu respuesta (1-3): ").strip()

        if respuesta in ("1", "2", "3"):
            return respuesta

        # Una entrada incorrecta no consume la pregunta.
        print("Opción no válida. Escribe 1, 2 o 3.")


def mostrar_resultado(aciertos, total):
    """Muestra la puntuación obtenida."""

    errores = total - aciertos
    porcentaje = aciertos / total * 100

    print("\n--- RESULTADO FINAL ---")
    print(f"Respuestas correctas: {aciertos}")
    print(f"Respuestas incorrectas: {errores}")
    print(f"Puntuación: {aciertos} de {total}")
    print(f"Porcentaje: {porcentaje:.1f}%")

    if aciertos == total:
        print("¡Respondiste todas correctamente!")

    elif porcentaje >= 50:
        print("¡Buen trabajo! Revisa las preguntas que fallaste.")

    else:
        print("Sigue practicando. Puedes volver a intentarlo.")


def jugar():
    """Realiza una partida completa del quiz."""

    aciertos = 0

    # copy crea una copia de la lista para cambiar su orden
    # sin modificar el orden de la lista original.
    preguntas_partida = PREGUNTAS.copy()

    # shuffle mezcla las preguntas.
    random.shuffle(preguntas_partida)

    total = len(preguntas_partida)

    # Evitamos iniciar una partida si la lista está vacía.
    if total == 0:
        print("Todavía no hay preguntas disponibles.")
        return

    # enumerate numera las preguntas comenzando desde 1.
    for numero, pregunta in enumerate(preguntas_partida, start=1):
        print(f"\n--- PREGUNTA {numero} DE {total} ---")

        # Accedemos al texto mediante su clave del diccionario.
        print(pregunta["pregunta"])

        # Mostramos las tres opciones de esta pregunta.
        for opcion in pregunta["opciones"]:
            print(opcion)

        respuesta = pedir_respuesta()

        if respuesta == pregunta["correcta"]:
            print("¡Respuesta correcta!")
            aciertos += 1

        else:
            print("Respuesta incorrecta.")

            # Las opciones se muestran desde 1,
            # pero las posiciones de la lista comienzan en 0.
            indice = int(pregunta["correcta"]) - 1
            correcta = pregunta["opciones"][indice]

            print(f"La respuesta correcta era: {correcta}")

        # Explicamos la respuesta para aprender durante el juego.
        print(pregunta["explicacion"])

    mostrar_resultado(aciertos, total)


def mostrar_menu():
    """Muestra las opciones del programa."""

    print("\n--- QUIZ DE PYTHON ---")
    print("1. Comenzar partida")
    print("2. Salir")


def main():
    """Repite el menú hasta que el usuario elija salir."""

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-2): ").strip()

        if opcion == "1":
            jugar()

        elif opcion == "2":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Elige 1 o 2.")


# Inicia el programa cuando ejecutamos este archivo directamente.
if __name__ == "__main__":
    main()