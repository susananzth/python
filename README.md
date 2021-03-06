# Python
Uso de python para programacion backend, desarrollo de domótica o inteligencia de las cosas, inteligencia artificial, data science.

Está en las aplicaciones más importantes del mercado actual, como google, instagram, uber, entre otros.
Tiene muchas ventajas, es fácil de leer y escribir, elegante al programar, maneja buenas prácticas para programar.

Premisa en python todo es un objeto!

## Conceptos

 * Algoritmo: Serie de pasos de forma ordenada para resolver un problema. Los serie de pasos no son infinitos, son pasos limitado y bien definidos para llegar a un fin, no debe ser ambiguo a la hora de indicar la resolución de problemas. Se puede ordenar los algoritmos con diagrama de flujo.

## Herramientas necesarias
* Un editor de código: puede ser sublime, brackets, atom, phpstorm, etc.
* Una terminal: para navegar entre las carpetas. puede ser cmd, el git bash, cmderk. Link: https://cmder.net/
* Python: el lenguaje que utilizaremos. Link: https://www.python.org/

## Comenzando…
Iniciar consola interactiva de python: ```py```
### Operadores aritméticos
* Suma: ```5 + 5```
* Resta: ```5 - 5```
* Multiplicación: ```5 * 5```
* División: ```10 / 5```
* Cociente: ```10 // 5```
* Resto: ```10 % 5```
* Potencia: ```5 ** 2```
* Raíz cuadrada: se debe importar la clase math, luego ejecutar la función ```math.sqrt()``` colocado como parámetro el número al cual se desea sacar la raiz cuadrada: ```math.sqrt(10)```
* Python respeta el orden de prioridad de las operaciones.

### Operadores lógicos
* ```and``` para determinar si el planteamiento se cumple o no, compara todas las variables.
* ```or``` busca que una de las variables se cumpla para determinar si el planteamiento se cumple o no.
* ```not``` da el valor contrario que está almacenado.
* ```==``` compara las variables, devuelve true o false.
* ```!=``` compara que los datos sean diferentes.
* ```>``` mayor que
* ```<``` menor que
* ```>=``` mayor igual que
* ```<=``` menor igual que



### Variables
* Concepto: un caja de almacenamiento en la memoria ram para guardar algún dato necesaria para el funcionamiento del programa, este dato puede variar a lo largo del funcionamiento del programa.
* Sintaxis: no debe comenzar con número, debe tener letras minúsculas y si es necesario separar las palabras, de debe usar guion bajo, no se admite espacios. Ej válidos: ```mi_variable```, ```variable50```, ```la5variable```.
* Asignación de variables: 
    - Interna: ```numero = 5```
    - Solicitando el dato al usuario: ```numero  = input(“Escriba un numero: ”)```


### Tipo de datos
* String: son cadena de caracteres que pueden contener números letras, espacios y caracteres especiales.
    - Formas de escritura: 
        ```
        nombre = “Susana”
        ```
        ```
        nombre = ‘Susana’
        ```
        ```
        texto_varias_lineas = “””
        Este es un string de varias líneas.
        En este texto se respetan los saltos de líneas
        “””
        ```

    - Formas de lectura:
        Consola: ```nombre```
        Editor de texto: ```print(nombre)```
    - Concatenación: ```nombre + ‘ ’ + nombre2```
    - Operaciones: ```nombre  + nombre```  ó  ```nombre  * 4```

* Número: son cadenas de números enteros o decimales, para el uso de decimales, solo basta con colocar punto para separar los decimales.
    - Formas de escritura: ```numero = 5```  ó  ```numero = 5.23```
    - Formas de lectura:
        Consola: ```numero ```
        Editor de texto: ```print(numero)```
    Concatenación: ```nombre + ‘ ’ + numero```
    Operaciones de string: ```numero + numero```  ó  ```numero * 4```

* Booleano: tipo de dato que determina el estado verdadero o falso.
    - Formas de escritura: ```pago_exisoto = True```  ó  ```pago_exisoto = False```
    - Formas de lectura:
        Consola: ```pago_exisoto```
        Editor de texto: ```print(pago_exisoto)```

* Conversión de datos

    Pasar texto a número: ```int()```
    ```
    numero1  = ‘5’
    numero2  = ‘5’
    numero1  + numero2 
    55
    numero1  = int(numero1)
    numero2 = int(numero2)
    numero1  + numero2 
    10
    ```
    Pasar número a texto: ```srt()```
    ```
    Texto = 4;
    Texto = str(Texto);
    Texto = '4';
    ```
    Pasar float: ```float()```

    - Ejercicio de ejemplo: [conversor.py](https://github.com/susananzth/python/blob/master/conversor.py)

### Condicionales

Declarar instrucciones en caso que el curso del programa vaya a tomar más de una ruta.
Importante que se deje la indentación con 4 espacios para la correcta compilación de las instrucciones
* Sintaxis
    ```
    if condicion: 
        pass
    elif condicion:
        pass
    else:
        pass
    ```
* Ejercicio de ejemplo: 
    [condicionales.py](https://github.com/susananzth/python/blob/master/codicionales.py)

### Funciones
Fragmentos de código que se puede llamar en diferentes partes del programa para no redundar codigo.
* Sintaxis
    ```
    # Declara la función
    def nombre_funcion():
        codigo de la funcion
    # Llama a la función
    nombre_funcion()
    ```
* Ejercicio de ejemplo:
    [funciones.py](https://github.com/susananzth/python/blob/master/funciones.py)

### Métodos
Son funciones para determinados objetos
* Sintaxis:
    ```
    objeto.nombre_metodo()
    ```
* Ejercicio de ejemplo:
    [metodos.py](https://github.com/susananzth/python/blob/master/metodos.py)

### Slices
Son fragmentos de string. Para obtenerlo, se le indica  la variable desde qué punto se tomará el fragmento de string.
* Sintaxis: 
    slice(comienza, finaliza, pasos)
    ```
    variable[0:3]
    ```
* Ejemplo: 
    ```
    nombre = ‘Susana’
	nombre[0:3]
    ```
    ```
    >>> Sus
    ```

### Palíndromo
Son palabras o frases que se leen igual al derecho y al revés.
* Ejercicio de ejemplo: [palindromo.py](https://github.com/susananzth/python/blob/master/palindromo.py)

### Bucles
Son repeticiones de situaciones. 
* Ejemplo de ciclo while: [bucles.py](https://github.com/susananzth/python/blob/master/bucles.py)
* Ejemplo de ciclo for: [bucle_for.py](https://github.com/susananzth/python/blob/master/bucle_for.py)

### Recorrer
Son funciones para recorrer string
* Ejercicio de ejemplo: [recorrer.py](https://github.com/susananzth/python/blob/master/recorrer.py) 

### Listas
Son objetos que pueden contener varios valores de tipos de datos diferentes. Es un elemento mutable, puede variar y cambiarse.
* Sintaxis: 
    ```
        # Declara la lista
        variable = [1, 3, 1, 5, 9, ‘Hola’, True]
        # Llama la lista indicando la posición del valor a mostrar.
        variable[0]
        #Agregar un elemento al final
        variable.addend(False)
        #Eliminar un elemento, indicando la posición del valor que deseo eliminar
        variable.pop(2)
    ```
### Tuplas
Son listas pero estáticas. Son inmutables, no se pueden cambiar.
* Sintaxis: tupla = (1, 3, 5, 9, 6)

### Diccionario
Son listas pero el indice no son números por defecto del 0 al infinito, sino que se pueden colocar un nombre, a este nombre se le denomina “Llave”.
* Sintaxis:
    ```
    diccionario = {
        ‘llave1’ = 1,
        ‘llave2’ = 2,
        ‘llave3’ = 3,
    }
    ```
* Ejercicio de ejemplo: [diccionario.py](https://github.com/susananzth/python/blob/master/diccionario.py)

## Ejercicios varios
* Prueba de primos: [prueba_primalidad.py](https://github.com/susananzth/python/blob/master/prueba_primalidad.py)
* Juego “Adivina el número”: [adivina_el_numero.py](https://github.com/susananzth/python/blob/master/adivina_el_numero.py)
* Generador de contraseña: [generador_contrasenas.py](https://github.com/susananzth/python/blob/master/generador_contrasenas.py)

