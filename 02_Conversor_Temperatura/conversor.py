"""Conversor de temperaturas para consola."""


# Convierte grados Celsius a Fahrenheit.
def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Convierte grados Fahrenheit a Celsius.
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# Solicita una temperatura y evita errores si se escribe texto.
def pedir_temperatura(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Escribe un número.")


# Muestra las opciones disponibles.
def mostrar_menu():
    print("\n--- CONVERSOR DE TEMPERATURA ---")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Salir")


# El bucle mantiene funcionando el programa hasta elegir salir.
while True:
    mostrar_menu()

    opcion = input("Elige una opción (1-3): ").strip()

    if opcion == "1":
        celsius = pedir_temperatura(
            "Escribe la temperatura en grados Celsius: "
        )

        fahrenheit = celsius_a_fahrenheit(celsius)

        # :.2f muestra solamente dos números después del punto decimal.
        print(f"{celsius:.2f} °C equivalen a {fahrenheit:.2f} °F")

    elif opcion == "2":
        fahrenheit = pedir_temperatura(
            "Escribe la temperatura en grados Fahrenheit: "
        )

        celsius = fahrenheit_a_celsius(fahrenheit)

        print(f"{fahrenheit:.2f} °F equivalen a {celsius:.2f} °C")

    elif opcion == "3":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Elige un número del 1 al 3.")