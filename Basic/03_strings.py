# Strings

my_string = "Hello, World!"
my_string2 = 'Hello, World!'
print(len(my_string))  # Devuelve la longitud de la variable
print(my_string[0])  # Devuelve el primer caracter de la variable
print(my_string[-1])  # Devuelve el último caracter de la variable
print(my_string[0:5])  # Devuelve los caracteres desde el índice 0 hasta el índice 5 (sin incluir el índice 5)
print(my_string[0:])  # Devuelve todos los caracteres desde el índice 0 hasta el final de la variable
print(my_string[:5])  # Devuelve los caracteres desde el inicio de la variable hasta el índice 5 (sin incluir el índice 5)
print(my_string[::2])  # Devuelve todos los caracteres de la variable, pero solo los caracteres en los índices pares
print(my_string[::-1])  # Devuelve todos los caracteres de la variable, pero en orden inverso

print(my_string.upper())  # Devuelve la variable en mayúsculas
print(my_string.lower())  # Devuelve la variable en minúsculas
print(my_string.replace("Hello", "Hola"))  # Reemplaza una subcadena por otra
print(my_string.split(","))  # Devuelve una lista con las subcadenas separadas por el separador especificado
print(my_string.strip())  # Elimina los espacios en blanco al inicio y al final de la variable
print(my_string.startswith("Hello"))  # Devuelve True si la variable empieza con la subcadena especificada
print(my_string.endswith("World!"))  # Devuelve True si la variable termina con la subcadena especificada
print(my_string.find("World"))  # Devuelve el índice de la primera aparición de la subcadena especificada, o -1 si no se encuentra
print(my_string.count("o"))  # Devuelve el número de apariciones de la subcadena especificada


print(my_string + "\ncon salto de linea")
print(my_string + "\tcon tabulación")

my_scape_string = "Hello, World!\tcon tabulacion y \\n con salto de linea"
print(my_scape_string)  # Devuelve la variable con los caracteres de escape interpretados

# Formateo de strings
my_name, my_surname, my_age = "Victor", "Vega", 30
print(f"Me llamo {my_name} {my_surname} y tengo {my_age} años.")
print("Me llamo {} {} y tengo {} años.".format(my_name, my_surname, my_age)) # Muestra el mismo resultado que la línea anterior 
print("Me llamo {0} {1} y tengo {2} años.".format(my_name, my_surname, my_age)) # Muestra el mismo resultado que la línea anterior
print("Me llamo %s %s y tengo %d años." % (my_name, my_surname, my_age)) # Muestra el mismo resultado que la línea anterior
#print("Me llamo %s %s y tengo %d años." % (my_name, my_surname, "hola")) # Muestra el mismo resultado que la línea anterior, pero con un string en lugar de un int
print("Me llamo {name} {surname} y tengo {age} años.".format(name=my_name, surname=my_surname, age=my_age)) # Muestra el mismo resultado que la línea anterior

## Desempaquetado de strings
language = "Python"
a, b, c, d, e, f = language
print(a)  # Devuelve 'P'
print(b)  # Devuelve 'y'

# Division de strings
my_string = "Hola, Mundo!"
my_string_slice = my_string[0:4]  # Devuelve 'Hola'
print(my_string_slice)

print(my_string[0:10:2]) # Devuelve 'HlaMnd' (desde el índice 0 hasta el índice 10, con un paso de 2)

print(language.capitalize())  # Devuelve 'Python' (la primera letra en mayúscula)
print(language.lower())  # Devuelve 'python' (todas las letras en minúscula)
print(language.upper())  # Devuelve 'PYTHON' (todas las letras en mayúscula)
print(language.count("o"))  # Devuelve 1 (el número de apariciones de la subcadena especificada)
print(language.title())  # Devuelve 'Python' (la primera letra de cada palabra en mayúscula)
print(language.swapcase())  # Devuelve 'pYTHON' (cambia mayúsculas por minúsculas y viceversa)
print(language.isupper())  # Devuelve False (si todas las letras son mayúsculas)
print(language.islower())  # Devuelve False (si todas las letras son minúsculas)
print(language.isalpha())  # Devuelve True (si todos los caracteres son alfabéticos)
print(language.isdigit())  # Devuelve False (si todos los caracteres son dígitos)
print(language.isalnum())  # Devuelve True (si todos los caracteres son alfanuméricos)
print(language.isspace())  # Devuelve False (si todos los caracteres son espacios en blanco)
print(language.isidentifier())  # Devuelve True (si todos los caracteres son válidos para un identificador)
print(language.isprintable())  # Devuelve True (si todos los caracteres son imprimibles) 


print(language.center(20, "-"))  # Devuelve '-------Python-------' (centra la cadena en un ancho de 20 caracteres, rellenando con '-')


