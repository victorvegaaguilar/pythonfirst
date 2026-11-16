# Variables

my_string_variable = "My cadena variable"
print(my_string_variable)


my_int_variable = 10
print(my_int_variable)

my_int_to_string_variable = str(my_int_variable)
print(my_int_to_string_variable)
print (type (my_int_to_string_variable))

my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, str(my_int_variable), str(my_bool_variable))

# Type NoneType
print(type (print(my_string_variable, str(my_int_variable), str(my_bool_variable))))

# Funciones

my_len = len(my_string_variable) # Devuelve la longitud de la variable
print(my_len)

print("Esta es mi variable", my_string_variable, "tiene", my_len, "caracteres")

# Variables en una sol linea. !Cuidado con abusar de esta sintaxis!
name,surname,alias,age = "Juan", "Perez", "JP", 30
#my_string_variable, my_int_variable, my_bool_variable = "My cadena variable", 5, False
print("Me llamo ", name, surname, "y mi alias es", alias, "y tengo", age, "años")

print(float(age))

# Input
"""
first_name = input("Ingrese su nombre: ")
age = input("Ingrese su edad: ")
print("Hola", first_name, "tienes", age, "años")
"""
# No se puede forzar el tipo de dato de una variable, pero se puede hacer un casting
"""
El tipado de python es dinámico, por lo que una variable puede cambiar de tipo 
en tiempo de ejecución
"""

address: str = "Mi dirección"

address = "32"

print(address)
print(type(address))
