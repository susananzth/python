# Definir función principal
def run():
    # Defino el diccionario, agrego los valores.
    mi_diccionario = {
        'llave1' : 1,
		'llave2' : 2,
		'llave3' : 3,
    }
    # Imprimo las llaves del diccionario utilizando una bucle for
    # Con '.keys()' estoy llamando a imprimir las llaves, no los valores.
    for llave in mi_diccionario.keys():
        print(llave)
    # Imprimo los valores del diccionario utilizando una bucle for
    # Con '.values()' estoy llamando a imprimir los valores.
    for valores in mi_diccionario.values():
        print(valores)
    # Imprimir las llaves y los valores utilizando '.items()'
    # Para esto, coloco las variables llave e items
    for llave, items in mi_diccionario.items():
        print("La llave: '" + llave + "' contiene el item: " + str(items))


if __name__ == '__main__':
    run()