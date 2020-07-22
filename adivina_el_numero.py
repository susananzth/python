# Módulo que contiene paquete de funciones para aleatoriedad
import random

# Definir función principal
def run():
    # Se genera un número aleatprio con '.randint()' como p arámetros se ingresa
    # el rango inicial y el final. Lo guardo en la variable 'numero_aleatorio'
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elige un npumero del 1 al 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Busca un número más grande!")
        else:
            print("Busca un número más pequeño!")
        numero_elegido = int(input("Elige otro número: "))
    print("Ganaste!")
    

if __name__ == '__main__':
    run()