# Módulo que contiene paquete de funciones para aleatoriedad
import random


def generar_contrasena():
    # Declaro 4 listas 
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minuscula = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos = ['*', '$', '%', '#', '@', '/', '&']
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # Sumo todas las listas
    caracteres = mayusculas + minuscula + simbolos + numeros
    # Guardo en la variable 'contrasena' un string aleatorio de lo guardado en 'caracteres'
    contrasena = []
    # El rando será la cantidad de vueltas que dará para elegir un caracter
    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
    
    contrasena = "".join(contrasena)
    return contrasena


# Definir función principal
def run():
    # Declaro la variable 'contrasena' donde almaceno lo arrojado por
    # pla función 'generar_contrasena'
    contrasena = generar_contrasena()
    print("Tu nueva contraseña es: " + contrasena)
    

if __name__ == '__main__':
    run()