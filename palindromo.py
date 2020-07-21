def palindromo(palabra):
    # Eliminar los espacios
    palabra = palabra.replace(" ", "")
    # Pasamos la palabra a minúscula
    palabra = palabra.lower()
    # Generar nueva variable que contenga la palabra invertida
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


#Como buena practica, se debe dejar dos saltos de linea despues de cada función.
# Creo una funcion principal que es la que correra el programa.
def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')

# Punto de entrada de un programa
# Cada vez que encuentra esto, correo todo el codigo que está debajo.
if __name__ == '__main__':
    run()