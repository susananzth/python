# Declaro la funcion utilizando la palabra reservada 'def'
# Segido del nombre de la funcion
def imprimir_mensaje():
    print("mensaje especial")
    print("¡Estoy aprendiendo Python!")

# Llamo la función
imprimir_mensaje()

# Otro ejemplo, para este caso utilizaremos un parámetro 'mensaje'
# El parámetro será ingresado por el usuario mediante la consola,
# Este dato es necesario para que se ejecute la funcion.
def conversacion(mensaje):
    print("Hola")
    print("¿Cómo estas?")
    print(mensaje)
    print("Adios")

# Almaceno en la variable 'opcion' lo obtenido por el usuario, lo convierto en entero con 'int()'
opcion = int(input("Elige una opción (1, 2, 3): "))
if opcion == 1:
    # Invoco la función y entre paentesis le paso el mensaje de parámetro.
    conversacion("Elegiste la opción 1")
elif opcion == 2:
    # Invoco la función y entre paentesis le paso el mensaje de parámetro.
    conversacion("Elegiste la opción 2")
elif opcion == 3:
    # Invoco la función y entre paentesis le paso el mensaje de parámetro.
    conversacion("Elegiste la opción 3")
else:
    print("Escribe la opción correcta")