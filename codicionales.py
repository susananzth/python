# Declaro la variable 'edad' donde ingreso el dato solicitado, 
# transformándolo en entero con 'int()'.
edad = int(input("Escribe tu edad: "))
if edad > 17: 
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')

# Otro ejemplo, esta vez utulizando elif.
numero = int(input("Escribe un numero: "))
if numero > 5: 
    print('Es mayor a 5')
elif numero == 5:
    print('Es igual a 5')
else:
    print('Es menor a 5')

# Otro ejemplo utilizando el conversor de divisas.

# En la variable 'menu' guardo un string de varias líneas.
menu = """
Bienvenido al converson de monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos
4 - Bolívares
5 - Soles

Elige una opción: """

# Almaceno en la variable 'opcion' lo obtenido por el usuario, el mensaje que le muestro 
# lo guardado en la variable 'menu', lo convierto en entero con 'int()'
opcion = int(input(menu))

if opcion == 1:
    """  Pesos colombianos a dólares  """
    moneda = input("¿Cuántos pesos colombianos tienes?: ")
    moneda = float(moneda)
    valor_dolar_hoy = 3875
    dolares = moneda / valor_dolar_hoy
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares.")
elif opcion == 2:
    """  Pesos argentinos a dólares  """
    moneda = input("¿Cuántos pesos argentinos tienes?: ")
    moneda = float(moneda)
    valor_dolar_hoy = 71.47
    dolares = moneda / valor_dolar_hoy
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares.")
elif opcion == 3:
    """  Pesos mexicanos a dólares  """
    moneda = input("¿Cuántos pesos mexicanos tienes?: ")
    moneda = float(moneda)
    valor_dolar_hoy = 22.54
    dolares = moneda / valor_dolar_hoy
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares.")
elif opcion == 4:
    """  Bolívares a dólares  """
    moneda = input("¿Cuántos Bolívares tienes?: ")
    moneda = float(moneda)
    valor_dolar_hoy = 219799.41
    dolares = moneda / valor_dolar_hoy
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares.")
elif opcion == 5:
    """  Soles a dólares  """
    moneda = input("¿Cuántos Soles tienes?: ")
    moneda = float(moneda)
    valor_dolar_hoy = 3.52
    dolares = moneda / valor_dolar_hoy
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares.")
else:
    print("Ingrese una opción correcta por favor")