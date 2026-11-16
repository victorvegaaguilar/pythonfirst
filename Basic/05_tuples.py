# Tuplas
my_empty_tuple = () # Declaración de una tupla vacía
print(my_empty_tuple)

my_tuple = (35, 1.70, "Juan", "Perez", )
print(my_tuple)
print(type(my_tuple)) # Devuelve el tipo de la variable

print(my_tuple[0]) # Devuelve el primer elemento de la tupla
print(my_tuple[-1]) # Devuelve el último elemento de la tupla
print(my_tuple[0:3]) # Devuelve los elementos desde el índice 0 hasta el índice 3 (sin incluir el índice 3)
print(my_tuple[::2]) # Devuelve todos los elementos de la tupla, pero solo los elementos en los índices pares
print(my_tuple[::-1]) # Devuelve todos los elementos de la tupla, pero en orden inverso

print(my_tuple.count("Juan")) # Devuelve el número de apariciones del elemento "Juan" en la tupla
print(my_tuple.index("Perez")) # Devuelve el índice del elemento "Perez" en la tupla

#my_tuple[1] = 1.80 # Error: TypeError: 'tuple' object does not support item assignment, ya que las tuplas son inmutables
print(my_tuple) # Devuelve la tupla original, ya que no se puede modificar

my_other_tuple = (1, 2, 3, 4, 5)
my_new_tuple = my_tuple + my_other_tuple # Concatenación de tuplas
print(my_new_tuple) # Devuelve la tupla concatenada

my_tuple2 = my_tuple * 2 # Repetición de tuplas
print(my_tuple2) # Devuelve la tupla repetida

my_tuple2 = list(my_tuple) # Conversión de tupla a lista
print(type(my_tuple2)) # Devuelve la lista convertida
my_tuple2.insert(1, 1.80) # Agrega un elemento en el índice 1 de la lista
print(my_tuple2) # Devuelve la lista con el nuevo elemento agregado
my_tuple2 = tuple(my_tuple2) # Conversión de lista a tupla
print(type(my_tuple2)) # Devuelve la tupla convertida

del my_tuple2 # Elimina la variable my_tuple2
# print(my_tuple2) # Error: NameError: name 'my_tuple2' is not defined, ya que la variable my_tuple2 ha sido eliminada


