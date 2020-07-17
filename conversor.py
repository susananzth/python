"""  Bolívares a dólares  """
# Solicito el dato al usuario y lo guardo en la variable 'bolivares'.
bolivares = input("¿Cuántos Bolívares tienes?: ")

# Convierto el string obtenido a número tipo decimal con 'float()'.
bolivares = float(bolivares)

# Creo una variable para el tipo de cambio a dolares llamada 'valor_dolar_hoy'.
valor_dolar_hoy = 219799.41

# Guardo en 'dolares' el resultado de la cantidad de 'bolivares' que indica el usuario entre el 'valor_dolar_hoy'.
dolares = bolivares / valor_dolar_hoy

# Redondeo los decimales utilizando 'round()' se ingresa dos parámetros, el dato a redondear y la cantidad de decimales que necesito.
dolares = round(dolares, 2)

# Convierto el float en la variable 'dolares' a string utilizando 'srt()'.
dolares = str(dolares)

# Imprimo en la consola concatenando texto y el resultado.
print("Tienes $" + dolares + " dólares.")


"""  Dólares a Bolívares  """
# Solicito el dato al usuario y lo guardo en la variable 'dolares'.
dolares = input("¿Cuántos Dólares tienes?: ")

# Convierto el string obtenido a número tipo decimal con 'float()'.
dolares = float(dolares)

# Creo una variable para el tipo de cambio a bolivares llamada 'valor_bolivar'.
valor_bolivar = 219799.41

# Guardo en 'bolivares' el resultado de la cantidad de 'dolares' que indica el usuario por el 'valor_bolivar'.
bolivares = dolares * valor_bolivar

# Redondeo los decimales utilizando 'round()' se ingresa dos parámetros, el dato a redondear y la cantidad de decimales que necesito.
bolivares = round(bolivares, 2)

# Convierto el float en la variable 'bolivares' a string utilizando 'srt()'.
bolivares = str(bolivares)

# Imprimo en la consola concatenando texto y el resultado.
print("Tienes " + bolivares + " Bs.F.")