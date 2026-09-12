"""Conversor de monedas con tasas ficticias para practicar."""

# Decimal permite realizar cálculos decimales con mayor precisión.
from decimal import Decimal, InvalidOperation


# Tasas de ejemplo: cantidad de cada moneda equivalente a 1 dólar.
# No representan cotizaciones actuales.
TASAS = {
    "USD": Decimal("1"),
    "CLP": Decimal("900"),
    "EUR": Decimal("0.90"),
}


def mostrar_monedas():
    """Muestra los códigos de las monedas disponibles."""

    print("\nMonedas disponibles:")
    print("USD: Dólar estadounidense")
    print("CLP: Peso chileno")
    print("EUR: Euro")


def pedir_moneda(mensaje):
    """Solicita una moneda hasta recibir un código válido."""

    while True:
        # upper convierte el texto a mayúsculas.
        # Así podemos escribir usd, Usd o USD.
        moneda = input(mensaje).strip().upper()

        if moneda in TASAS:
            return moneda

        print("Moneda no válida. Escribe USD, CLP o EUR.")


def pedir_cantidad():
    """Solicita una cantidad positiva y con hasta dos decimales."""

    while True:
        texto = input(
            "Cantidad, sin separadores de miles: "
        ).strip().replace(",", ".")

        try:
            cantidad = Decimal(texto)

            # Rechazamos valores especiales como NaN o Infinity.
            if not cantidad.is_finite():
                print("Escribe un número finito.")
                continue

            if cantidad <= 0:
                print("La cantidad debe ser mayor que cero.")
                continue

            # Limitamos el tamaño para este ejercicio.
            if cantidad > Decimal("1000000000000"):
                print("La cantidad máxima es 1000000000000.")
                continue

            # quantize ajusta el número a dos decimales.
            redondeada = cantidad.quantize(Decimal("0.01"))

            if cantidad != redondeada:
                print("Escribe una cantidad con hasta dos decimales.")
                continue

            return redondeada

        except InvalidOperation:
            print("Entrada no válida. Ejemplo: 1500 o 1500,50.")


def convertir_moneda(cantidad, origen, destino):
    """Convierte una cantidad usando el dólar como referencia."""

    # Primero convertimos la cantidad original a dólares.
    dolares = cantidad / TASAS[origen]

    # Después convertimos los dólares a la moneda de destino.
    resultado = dolares * TASAS[destino]

    return resultado


def realizar_conversion():
    """Solicita los datos y muestra la conversión."""

    mostrar_monedas()

    origen = pedir_moneda("Moneda de origen: ")
    destino = pedir_moneda("Moneda de destino: ")
    cantidad = pedir_cantidad()

    resultado = convertir_moneda(cantidad, origen, destino)

    # :.2f muestra el número con dos decimales.
    print(
        f"\n{cantidad:.2f} {origen} "
        f"equivalen a {resultado:.2f} {destino}"
    )

    print("Resultado calculado con tasas ficticias de práctica.")


def mostrar_tasas():
    """Muestra las tasas utilizadas por el programa."""

    print("\n--- TASAS FICTICIAS ---")

    # items permite recorrer las claves y valores del diccionario.
    for moneda, tasa in TASAS.items():
        print(f"1 USD = {tasa:.2f} {moneda}")


def mostrar_menu():
    """Muestra las opciones del conversor."""

    print("\n--- CONVERSOR DE MONEDAS ---")
    print("1. Convertir monedas")
    print("2. Ver tasas de ejemplo")
    print("3. Salir")


def main():
    """Mantiene funcionando el programa hasta elegir salir."""

    print("Proyecto educativo: utiliza tasas ficticias.")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-3): ").strip()

        if opcion == "1":
            realizar_conversion()

        elif opcion == "2":
            mostrar_tasas()

        elif opcion == "3":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Elige 1, 2 o 3.")


# Inicia el programa cuando ejecutamos este archivo directamente.
if __name__ == "__main__":
    main()

            
            
                