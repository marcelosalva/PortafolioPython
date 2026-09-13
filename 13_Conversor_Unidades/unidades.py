"""Conversor de unidades de longitud y masa para consola."""

# math permite comprobar que un número no sea infinito ni NaN.
import math


# Cada factor indica cuántos metros representa una unidad.
LONGITUD = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
}


# Cada factor indica cuántos gramos representa una unidad.
MASA = {
    "mg": 0.001,
    "g": 1.0,
    "kg": 1000.0,
    "t": 1000000.0,
}


def pedir_cantidad():
    """Solicita una cantidad válida, mayor o igual que cero."""

    while True:
        texto = input(
            "Cantidad, sin separadores de miles: "
        ).strip().replace(",", ".")

        try:
            cantidad = float(texto)

            # Rechazamos valores especiales como inf y nan.
            if not math.isfinite(cantidad):
                print("Escribe un número finito.")
                continue

            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
                continue

            return cantidad

        except ValueError:
            print("Entrada no válida. Ejemplo: 1500 o 2,5.")


def pedir_unidad(mensaje, factores):
    """Solicita una unidad incluida en el diccionario."""

    while True:
        # lower permite aceptar KM, Km o km.
        unidad = input(mensaje).strip().lower()

        if unidad in factores:
            return unidad

        print("Unidad no válida. Usa una de las unidades disponibles.")


def convertir(cantidad, origen, destino, factores):
    """Convierte pasando primero por la unidad de referencia."""

    # Para longitud, la referencia es el metro.
    # Para masa, la referencia es el gramo.
    cantidad_base = cantidad * factores[origen]

    resultado = cantidad_base / factores[destino]

    return resultado


def realizar_conversion(factores, titulo):
    """Solicita los datos y muestra el resultado."""

    print(f"\n--- {titulo} ---")

    # join une los códigos del diccionario en un texto.
    print("Unidades disponibles: " + ", ".join(factores))

    origen = pedir_unidad("Unidad de origen: ", factores)
    destino = pedir_unidad("Unidad de destino: ", factores)
    cantidad = pedir_cantidad()

    resultado = convertir(cantidad, origen, destino, factores)

    # Un número demasiado grande puede superar el límite de float.
    if not math.isfinite(resultado):
        print("La cantidad es demasiado grande para esta conversión.")
        return

    # Detectamos si un valor muy pequeño se perdió en el cálculo.
    if cantidad > 0 and resultado == 0:
        print("La cantidad es demasiado pequeña para esta conversión.")
        return

    # .10g muestra hasta diez cifras significativas.
    # Así podemos mostrar cantidades pequeñas sin fijar dos decimales.
    print(
        f"\n{cantidad:.10g} {origen} "
        f"equivalen a {resultado:.10g} {destino}"
    )


def mostrar_menu():
    """Muestra las categorías disponibles."""

    print("\n--- CONVERSOR DE UNIDADES ---")
    print("1. Longitud: mm, cm, m, km")
    print("2. Masa: mg, g, kg, t")
    print("3. Salir")


def main():
    """Repite el menú hasta elegir salir."""

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-3): ").strip()

        if opcion == "1":
            realizar_conversion(LONGITUD, "LONGITUD")

        elif opcion == "2":
            realizar_conversion(MASA, "MASA")

        elif opcion == "3":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Elige 1, 2 o 3.")


# Inicia el programa al ejecutar este archivo directamente.
if __name__ == "__main__":
    main()