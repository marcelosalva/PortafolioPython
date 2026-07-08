import math

"""Calculadora para consola con varias operaciones e historial."""


# Cada operación está dentro de una función.
# Las funciones reciben números, realizan una tarea y devuelven el resultado.
def sumar(numero_1, numero_2):
    return numero_1 + numero_2


def restar(numero_1, numero_2):
    return numero_1 - numero_2


def multiplicar(numero_1, numero_2):
    return numero_1 * numero_2


def dividir(numero_1, numero_2):
    return numero_1 / numero_2


def calcular_potencia(base, exponente):
    return base**exponente


def calcular_raiz(numero):
    return math.sqrt(numero)


def calcular_porcentaje(numero, porcentaje):
    return numero * porcentaje / 100


def calcular_resto(numero_1, numero_2):
    return numero_1 % numero_2


def calcular_valor_absoluto(numero):
    return abs(numero)


# Esta función solicita un número hasta que el usuario escribe uno válido.
def pedir_numero(mensaje):
    while True:
        try:
            # float permite usar números enteros y decimales.
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Por favor, escribe un número.")


# Esta función muestra todas las opciones disponibles.
def mostrar_menu():
    print("\n---- CALCULADORA ----")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Porcentaje")
    print("8. Resto de una división")
    print("9. Valor absoluto")
    print("10. Ver historial")
    print("11. Salir")


# Esta lista guardará las operaciones realizadas durante la ejecución.
historial = []


# El bucle repite el menú hasta que el usuario elige salir.
while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-11): ").strip()

    if opcion == "11":
        print("¡Hasta luego!")
        break

    elif opcion == "10":
        print("\n---- HISTORIAL ----")

        # Una lista vacía se considera False en Python.
        if not historial:
            print("Todavía no has realizado operaciones.")
        else:
            # enumerate permite numerar los elementos empezando desde 1.
            for posicion, operacion in enumerate(historial, start=1):
                print(f"{posicion}. {operacion}")

    elif opcion == "6":
        numero = pedir_numero("Escribe un número: ")

        if numero < 0:
            print("Error: no se puede calcular la raíz real de un número negativo.")
        else:
            resultado = calcular_raiz(numero)
            texto = f"Raíz cuadrada de {numero} = {resultado}"
            print(f"Resultado: {texto}")
            historial.append(texto)

    elif opcion == "9":
        numero = pedir_numero("Escribe un número: ")
        resultado = calcular_valor_absoluto(numero)
        texto = f"Valor absoluto de {numero} = {resultado}"
        print(f"Resultado: {texto}")
        historial.append(texto)

    elif opcion in ("1", "2", "3", "4", "5", "7", "8"):
        numero_1 = pedir_numero("Escribe el primer número: ")

        # La opción de porcentaje utiliza un mensaje más específico.
        if opcion == "7":
            numero_2 = pedir_numero("Escribe el porcentaje: ")
        else:
            numero_2 = pedir_numero("Escribe el segundo número: ")

        if opcion == "1":
            resultado = sumar(numero_1, numero_2)
            texto = f"{numero_1} + {numero_2} = {resultado}"

        elif opcion == "2":
            resultado = restar(numero_1, numero_2)
            texto = f"{numero_1} - {numero_2} = {resultado}"

        elif opcion == "3":
            resultado = multiplicar(numero_1, numero_2)
            texto = f"{numero_1} * {numero_2} = {resultado}"

        elif opcion == "4":
            if numero_2 == 0:
                print("Error: no se puede dividir por cero.")
                continue

            resultado = dividir(numero_1, numero_2)
            texto = f"{numero_1} / {numero_2} = {resultado}"

        elif opcion == "5":
            resultado = calcular_potencia(numero_1, numero_2)
            texto = f"{numero_1} ^ {numero_2} = {resultado}"

        elif opcion == "7":
            resultado = calcular_porcentaje(numero_1, numero_2)
            texto = f"{numero_2}% de {numero_1} = {resultado}"

        else:
            if numero_2 == 0:
                print("Error: no se puede calcular el resto al dividir por cero.")
                continue

            resultado = calcular_resto(numero_1, numero_2)
            texto = f"Resto de {numero_1} / {numero_2} = {resultado}"

        # Esta parte es común para todas las operaciones de dos números.
        print(f"Resultado: {texto}")
        historial.append(texto)

    else:
        print("Opción no válida. Elige un número del 1 al 11.")
