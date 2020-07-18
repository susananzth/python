# Declaro la funcion utilizando la palabra reservada 'def'
# Seguido del nombre de la funcion
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

# Solicito una opción al usuario, transformo el dato string a entero con 'int()'.
# Declaro la variable 'opcion' donde guardo el dato solicitado.
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

# Otro ejemplo utilizando el conversor de divisas: https://github.com/susananzth/python/blob/master/conversor.py
def conversor (tipo_divisa, valor_dolar_hoy):
    moneda = input("¿Cuántos " + tipo_divisa + " tienes?: ")
    moneda = float(moneda)
    dolares = moneda / valor_dolar_hoy
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares.")

# En la variable 'menu' guardo un string de varias líneas.
menu = """
Bienvenido al converson de monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos
4 - Bolívares
5 - Soles

Elige una opción: """

# Solicito una opción al usuario (el mensaje que le muestro es el almacenado en 
# la variable 'menu'), transformo el dato string a entero con 'int()'.
# Declaro la variable 'opcion' donde guardo el dato solicitado.
opcion = int(input(menu))

if opcion == 1:
    """  Pesos colombianos a dólares  """
    conversor("Pesos colombianos", 3875)
elif opcion == 2:
    """  Pesos argentinos a dólares  """
    conversor("Pesos argentinos", 71.47)
elif opcion == 3:
    """  Pesos mexicanos a dólares  """
    conversor("Pesos mexicanos", 22.54)
elif opcion == 4:
    """  Bolívares a dólares  """
    conversor("Bolívares", 219799.41)
elif opcion == 5:
    """  Soles a dólares  """
    conversor("Soles", 3.52)
else:
    print("Ingrese una opción correcta por favor")