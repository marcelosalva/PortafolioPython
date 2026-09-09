import random

"""juego de adivinar un numero para consola """

def pedir_numero(mensaje):
    """pide u numero entero y repite hasta  que el usuario escriba uno valido """
    
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        
        except ValueError:
            print("entrada no valida. escribe un numero entero")
            
def jugar():
    """ejecuta una partida del juego """
    
    numero_secreto =random.randint(1, 100)
    intentos = 0 
    
    print("\nestoy pensando en un numero del 1 al 100")
    print("intenta adivinarlo")
    
    
    while True:
          respuesta = pedir_numero("escribe tu numero: ")
          intentos += 1
          
          if respuesta < numero_secreto:
              print("el numero secreto es mayor ")
              
          elif respuesta > numero_secreto:
              print("el numero secreto es menor ")
              
          else:
              print(f"correcto adivinaste el numero en {intentos} intentos  ")
              
              
def mostrar_menu():
    """muestra las opciones disponibles"""
    
    print("\n--- ADIVINA EL NÚMERO ---")
    print("1. jugar")
    print("2.  salir" ) 
    
                                               
while True:
    mostrar_menu()
    opcion = input("elige una opcion (1-2): ").strip()
    
    if opcion == "1":
        jugar()
        
    elif opcion == "2":
        print("hasta luego")
        break
    
    else:
        print("opcion no valida elige 1 o 2 ")                                                   