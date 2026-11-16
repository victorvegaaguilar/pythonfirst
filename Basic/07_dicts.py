# Diccionarios

my_dict = {} # Declaración de un diccionario vacío
print(my_dict)
print(type(my_dict)) # Devuelve el tipo de la variable
my_other_dict = dict() # Declaración de un diccionario vacío
print(my_other_dict)
print(type(my_other_dict)) # Devuelve el tipo de la variable

my_other_dict = {"Nombre": "Juan", "Apellido": "Perez", "Edad": 30, "Estatura": 1.70}
print(my_other_dict)
print(my_other_dict["Nombre"]) # Devuelve el valor de la clave "Nombre"
my_other_dict["Nombre"] = "Pedro" # Modifica el valor de la clave "Nombre"
print(my_other_dict)

my_dict = {
    "Nombre": "Juan",
    "Apellido": "Perez",
    "Edad": 30,
    "Estatura": 1.70,
    "Hobbies": ["Correr", "Leer", "Programar"],
    "Mascotas": {"Perro": "Firulais", "Gato": "Michi"},
    1: "Valor de la clave 1",
}
print(my_dict)

print(my_dict["Hobbies"]) # Devuelve el valor de la clave "Hobbies"
print(my_dict["Hobbies"][1]) # Devuelve el valor del índice 1 de la lista de la clave "Hobbies"
print(my_dict["Mascotas"]["Gato"]) # Devuelve el valor de la clave "Gato" del diccionario de la clave "Mascotas"
print(my_dict[1]) # Devuelve el valor de la clave 1
print(len(my_dict)) # Devuelve la longitud del diccionario
print("Nombre" in my_dict) # Devuelve True si la clave "Nombre" está en el diccionario, False si no lo está
my_dict["Nombre"] = "Pedro" # Modifica el valor de la clave "Nombre"
print(my_dict)
print(my_dict[1]) # Devuelve el valor de la clave 1

print(my_dict.keys()) # Devuelve las claves del diccionario
print(my_dict.values()) # Devuelve los valores del diccionario
print(my_dict.items()) # Devuelve los elementos del diccionario como tuplas (clave, valor)

del my_dict[1] # Elimina la clave 1 del diccionario
print(my_dict)
print(my_dict.fromkeys(["Nombre", "Apellido", "Edad"])) # Crea un nuevo diccionario con las claves especificadas y un valor por defecto

my_new_dict = dict.fromkeys(["Nombre", "Apellido", "Edad"], "Valor por defecto") # Crea un nuevo diccionario con las claves especificadas y un valor por defecto

print(my_new_dict) # Devuelve el nuevo diccionario

my_new_dict2 = dict.fromkeys(my_dict) # Crea un nuevo diccionario con las claves del diccionario my_dict y un valor por defecto
print(my_new_dict2) # Devuelve el nuevo diccionario

