# Función 'es_primo' agregando como parámetro un número
def es_primo(numero):
    # Declaro un contador inicianizándolo en cero
    contador = 0
    for i in range(1, numero +1):
        if i == 1 or i == numero:
           continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False


# Definir función principal
def run():
    # Guardo en la variable 'numero' el dato ingresado por el usuario,
    # convirtiéndolo en entero con la función 'int()'
    numero = int(input("Escribe un número: "))
    # Agrego la condicional, haciendo la pregunta ¿Si es primo? indicando como 
    # parámetro el dato almacenado en la variable 'numero'
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")


if __name__ == '__main__':
    run()