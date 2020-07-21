# Definir función principal
def run():
    # Guardo en la variable, el dato solicitado al usuario.
    nombre = input('Escribe tu nombre: ')
    # Inicio el bucle indicando que por cada letra que contenga el nombre,
    # las recorra una por una imprimiendo cada letra convirtiendola en mayúscula.
    for letra in nombre:
        print(letra.upper())


if __name__ == '__main__':
    run()