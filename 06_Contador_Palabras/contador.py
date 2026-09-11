"""Contador de palabras para consola."""


def contar_palabras(texto):
    """Cuenta cuántas palabras tiene un texto."""

    palabras = texto.split()
    return len(palabras)


def contar_caracteres(texto):
    """Cuenta cuántos caracteres tiene un texto."""

    return len(texto)


def contar_vocales(texto):
    """Cuenta cuántas vocales tiene un texto."""

    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    cantidad = 0

    for letra in texto:
        if letra in vocales:
            cantidad += 1

    return cantidad


def contar_frecuencia_palabras(texto):
    """Cuenta cuántas veces aparece cada palabra."""

    palabras = texto.lower().split()
    frecuencia = {}

    for palabra in palabras:
        palabra = palabra.strip(".,;:¡!¿?()[]{}\"'")

        if palabra != "":
            if palabra in frecuencia:
                frecuencia[palabra] += 1
            else:
                frecuencia[palabra] = 1

    return frecuencia


def mostrar_frecuencia(frecuencia):
    """Muestra la frecuencia de cada palabra."""

    if not frecuencia:
        print("No hay palabras para mostrar.")
    else:
        print("\nFrecuencia de palabras:")

        for palabra, cantidad in frecuencia.items():
            print(f"{palabra}: {cantidad}")


def mostrar_menu():
    """Muestra las opciones disponibles."""

    print("\n--- CONTADOR DE PALABRAS ---")
    print("1. Analizar texto")
    print("2. Salir")


while True:
    mostrar_menu()

    opcion = input("Elige una opción (1-2): ").strip()

    if opcion == "1":
        texto = input("Escribe un texto: ")

        total_palabras = contar_palabras(texto)
        total_caracteres = contar_caracteres(texto)
        total_vocales = contar_vocales(texto)
        frecuencia = contar_frecuencia_palabras(texto)

        print("\n--- RESULTADOS ---")
        print(f"Palabras: {total_palabras}")
        print(f"Caracteres: {total_caracteres}")
        print(f"Vocales: {total_vocales}")

        mostrar_frecuencia(frecuencia)

    elif opcion == "2":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Elige 1 o 2.")