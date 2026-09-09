import secrets
import string

"""generador de contraseñas  seguras para consola."""

def pedir_longitud():
    """Solicita una longitud valida para la contraseña. """
    
    while True:
        try:
            longitud = int(
                input("¿cuantos  caracteres tendra la contraseña?: ")
                
            )
            
            #necesitamos al menos cuatro caracteres para incluir 
            #una minidcula, mayuscula, numero y simbolo.
            if longitud < 4:
                print("la contraseña debe tener la menos 4 caracteres")
                
            else:
                return longitud
            
        except ValueError:
            print("entrada no valida . escribe un unmero entero ")
            

def generar_contrasenas(longitud):
    """generar una contraseña con diferente tipos de caracteres"""
    
    
    #escogemos al menos un caracter de cada categoria
    caracteres = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]                    
    
    #juntamos todos los caracteres que podremos utilizar
    opciones = (
         string.ascii_lowercase
         + string.ascii_uppercase
          + string.digits
         + string.punctuation
)
    
    # completamos la contraseña hasta alcanzar la longitud solicitado
    for _ in range(longitud - 4):
        caracteres.append(secrets.choice(opciones))
        
        
    #mezclamos  los caracteres para que no aparezcan siempre
    #en el mismo orden
    secrets.SystemRandom().shuffle(caracteres)
    
    #join convierte la lista de caracteres en una solo texto
    return "".join(caracteres)

def mostrar_menu():
    """muestra las opciones disponibles """
    
    print("\n--- GENERADOR DE CONTRASEÑAS ---")
    print("1. generar contraseña")
    print("2. salir")
    

while True:
    mostrar_menu()
    
    opcion = input("elige una opcion (1-2): ").strip()
    
    if opcion == "1":
        longitud = pedir_longitud()
        contrasena = generar_contrasenas(longitud)
        
        print(f"contraseña generada: {contrasena}")
        
    elif opcion == "2":
        print("hasta luego")
        break
    
    else:
        print("opcion no valida. elige 1 o 2")        
        