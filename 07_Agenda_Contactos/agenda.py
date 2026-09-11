"""Agenda de contactos para consola."""

# json permite guardar y leer datos en un archivo de texto organizado.
import json

# Path permite indicar dónde está nuestro archivo de contactos.
from pathlib import Path


# Los contactos se guardarán en la misma carpeta que agenda.py.
ARCHIVO = Path(__file__).parent / "contactos.json"


def cargar_contactos():
    """Lee los contactos guardados anteriormente."""

    # Si el archivo no existe, comenzamos con un diccionario vacío.
    if not ARCHIVO.exists():
        return {}

    # "r" significa leer. with cierra el archivo automáticamente.
    with ARCHIVO.open("r", encoding="utf-8") as archivo:
        contactos = json.load(archivo)

    # Nuestra agenda debe ser un diccionario de nombres y teléfonos.
    if not isinstance(contactos, dict):
        raise ValueError("El archivo no contiene una agenda válida.")

    for nombre, telefono in contactos.items():
        if not isinstance(nombre, str) or not isinstance(telefono, str):
            raise ValueError("Hay un contacto con formato incorrecto.")

    return contactos


def guardar_contactos(contactos):
    """Guarda los contactos y avisa si lo consiguió."""

    try:
        # "w" significa escribir y reemplazar el contenido anterior.
        with ARCHIVO.open("w", encoding="utf-8") as archivo:
            # indent hace que el archivo sea fácil de leer.
            # ensure_ascii=False permite guardar los acentos.
            json.dump(
                contactos,
                archivo,
                ensure_ascii=False,
                indent=4,
            )

        return True

    except OSError:
        print("No se pudieron guardar los cambios.")
        return False


def pedir_texto(mensaje):
    """Pide un texto hasta que el usuario escriba algo."""

    while True:
        # strip elimina los espacios del principio y del final.
        texto = input(mensaje).strip()

        if texto:
            return texto

        print("No puedes dejar este campo vacío.")


def encontrar_contacto(contactos, nombre):
    """Busca un nombre sin distinguir mayúsculas y minúsculas."""

    for nombre_guardado in contactos:
        if nombre_guardado.casefold() == nombre.casefold():
            return nombre_guardado

    # None indica que no encontramos el contacto.
    return None


def agregar_contacto(contactos):
    """Agrega un nombre y un teléfono a la agenda."""

    nombre = pedir_texto("Nombre del contacto: ")

    # Evitamos guardar dos contactos con el mismo nombre.
    if encontrar_contacto(contactos, nombre) is not None:
        print("Ya existe un contacto con ese nombre.")
        return

    # Guardamos el teléfono como texto para conservar + y ceros iniciales.
    telefono = pedir_texto("Teléfono: ")

    # El nombre es la clave del diccionario y el teléfono es su valor.
    contactos[nombre] = telefono

    if guardar_contactos(contactos):
        print("Contacto agregado y guardado.")
    else:
        # Deshacemos el cambio si no se pudo guardar.
        del contactos[nombre]


def ver_contactos(contactos):
    """Muestra los contactos ordenados por nombre."""

    # Un diccionario vacío se considera falso.
    if not contactos:
        print("Todavía no tienes contactos.")
        return

    print("\n--- CONTACTOS ---")

    # sorted ordena los nombres sin distinguir mayúsculas.
    for nombre in sorted(contactos, key=str.casefold):
        print(f"{nombre}: {contactos[nombre]}")


def buscar_contacto(contactos):
    """Busca un contacto por su nombre completo."""

    nombre = pedir_texto("Nombre que quieres buscar: ")
    encontrado = encontrar_contacto(contactos, nombre)

    if encontrado is None:
        print("No se encontró ese contacto.")
    else:
        print(f"{encontrado}: {contactos[encontrado]}")


def eliminar_contacto(contactos):
    """Pide confirmación antes de eliminar un contacto."""

    nombre = pedir_texto("Nombre del contacto que quieres eliminar: ")
    encontrado = encontrar_contacto(contactos, nombre)

    if encontrado is None:
        print("No se encontró ese contacto.")
        return

    confirmacion = input(
        f"¿Eliminar a {encontrado}? (s/n): "
    ).strip().lower()

    if confirmacion != "s":
        print("Eliminación cancelada.")
        return

    # pop elimina el contacto y devuelve su teléfono.
    telefono = contactos.pop(encontrado)

    if guardar_contactos(contactos):
        print("Contacto eliminado.")
    else:
        # Recuperamos el contacto si no se pudo guardar.
        contactos[encontrado] = telefono


def mostrar_menu():
    """Muestra las opciones de la agenda."""

    print("\n--- AGENDA DE CONTACTOS ---")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")


def main():
    """Carga los contactos y ejecuta el menú."""

    try:
        contactos = cargar_contactos()

    except (OSError, ValueError):
        # Detenemos el programa si el archivo no se puede leer
        # o tiene un formato incorrecto, para no sobrescribirlo.
        print("No se pudo leer contactos.json.")
        print("Revisa el archivo antes de continuar.")
        return

    # Este bucle mantiene funcionando la agenda hasta elegir salir.
    while True:
        mostrar_menu()

        opcion = input("Elige una opción (1-5): ").strip()

        if opcion == "1":
            agregar_contacto(contactos)

        elif opcion == "2":
            ver_contactos(contactos)

        elif opcion == "3":
            buscar_contacto(contactos)

        elif opcion == "4":
            eliminar_contacto(contactos)

        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Elige un número del 1 al 5.")


# Ejecuta main cuando iniciamos este archivo directamente con Python.
if __name__ == "__main__":
    main()
