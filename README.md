# Python
Uso de python para programacion backend, desarrollo de domótica o inteligencia de las cosas, inteligencia artificial, data science.

Está en las aplicaciones más importantes del mercado actual, como google, instagram, uber, entre otros.
Tiene muchas ventajas, es fácil de leer y escribir, elegante al programar, maneja buenas prácticas para programar.

Premisa en python todo es un objeto!

## Conceptos

 *Algoritmo: Serie de pasos de forma ordenada para resolver un problema. Los serie de pasos no son infinitos, son pasos limitado y bien definidos para llegar a un fin, no debe ser ambiguo a la hora de indicar la resolución de problemas. Se puede ordenar los algoritmos con diagrama de flujo.

## Herramientas necesarias
* Un editor de código: puede ser sublime, brackets, atom, phpstorm, etc.
* Una terminal: para navegar entre las carpetas. puede ser cms, el git bash, cmderk. Link: https://cmder.net/
* Python: el lenguaje que utilizaremos. Link: https://www.python.org/

## Comenzando…
Iniciar consola interactiva de python: py
### Operadores aritméticos
Suma: 5 + 5
Resta: 5 - 5
Multiplicación: 5 * 5
División: 10 / 5
Cociente: 10 // 5
Resto: 10 % 5
Potencia: 5 ** 2
Raíz cuadrada: se debe importar la clase math, luego ejecutar la función math.sqrt() colocado como parámetro el número al cual se desea sacar la raiz cuadrada: math.sqrt(10)
Python respeta el orden de prioridad de las operaciones.

Operadores lógicos
and: para determinar si el planteamiento se cumple o no, compara todas las variables.
or: busca que una de las variables se cumpla para determinar si el planteamiento se cumple o no.
not: da el valor contrario que está almacenado.
== compara las variables, devuelve true o false.
!= compara que los datos sean diferentes.
> mayor que
< menor que
>= mayor igual que
<= menor igual que



Variables
Concepto: un caja de almacenamiento en la memoria ram para guardar algún dato necesaria para el funcionamiento del programa, este dato puede variar a lo largo del funcionamiento del programa.
Sintaxis: no debe comenzar con número, debe tener letras minúsculas y si es necesario separar las palabras, de debe usar guion bajo, no se admite espacios. Ej válidos: mi_variable, variable50, la5variable
Asignación de variables: 
Interna: numero = 5
Solicitando el dato al usuario: numero  = input(“Escriba un numero: ”)


Tipo de datos
String: son cadena de caracteres que pueden contener números letras, espacios y caracteres especiales.
Formas de escritura:
nombre = “Susana” 
nombre = ‘Susana’
Formas de lectura:
Consola: nombre
Editor de texto: print(nombre)
Concatenación:
nombre + ‘ ’ + nombre2
Operaciones:
nombre  + nombre 
nombre  * 4

Número: son cadenas de números enteros o decimales, para el uso de decimales, solo basta con colocar punto para separar los decimales.
Formas de escritura:
numero = 5 
numero = 5.23
Formas de lectura:
Consola: numero 
Editor de texto: print(numero)
Concatenación:
nombre + ‘ ’ + numero 
Operaciones de string:
numero + numero 
numero * 4

Booleano: tipo de dato que determina el estado verdadero o falso.
Formas de escritura:
pago_exisoto = True 
pago_exisoto = False
Formas de lectura:
Consola: pago_exisoto
Editor de texto: print(pago_exisoto)

Conversión de datos
Pasar texto a número: int()
numero1  = ‘5’
numero2  = ‘5’
numero1  + numero2 
55
numero1  = int(numero1)
numero2 = int(numero2)
numero1  + numero2 
10
Pasar número a texto: srt()
Texto = 4;
Texto = str(Texto);
Texto = '4';
Pasar float: float()
