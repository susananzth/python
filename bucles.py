# Bucle while (mientras)
# Definir función principal
def run():
    # Definino una constante, para esto colocamos el nombre en mayúscula.
    LIMITE = 1000
    # Defino la variable del contador.
    contador = 0
    # Defino la variable de la potencia.
    potencia_2 = 2**contador
    # Definio el bucle while, mientras la condición se cumpla, ejecutará el código.
    while potencia_2 < LIMITE:
        print('2 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2))
        # Aumento el contador para que no haya un bulcle infinito.
        contador = contador + 1
        potencia_2 = 2**contador

if __name__ == '__main__':
    run()