# Sets

my_empty_set = set() # Declaración de un set vacío
print(my_empty_set)

my_set = {1, 2, 3, 4, "Hola", 2.52}
print(my_set)
print(type(my_set)) # Devuelve el tipo de la variable
print(len(my_set)) # Devuelve la longitud del set
print(my_set) # Devuelve el set original
#print(my_set[0]) # Error: TypeError: 'set' object is not subscriptable, ya que los sets no son indexables
print(1 in my_set) # Devuelve True si el elemento 1 está en el set, False si no lo está
my_set.add("Nuevo") # Agrega un elemento al set
print(my_set) # Devuelve el set con el nuevo elemento agregado
#my_set.remove(6) # Elimina un elemento del set
print(my_set) # Devuelve el set con el elemento eliminado
my_set.discard(6) # Elimina un elemento del set, pero no lanza un error si el elemento no está en el set
print(my_set) # Devuelve el set con el elemento eliminado
my_set.clear() # Elimina todos los elementos del set
print(my_set) # Devuelve el set vacío

print("Hola" in my_set) # Devuelve False, ya que el set está vacío
print("Hola" not in my_set) # Devuelve True, ya que el set está vacío

my_set_data = {"Juan", "Perez", 3, 4.3}
print(my_set_data)
my_set_data.add("Nuevo") # Agrega un elemento al set
print(my_set_data) # Devuelve el set con el nuevo elemento agregado

del my_set_data # Elimina la variable my_set_data
#print(my_set_data) # Error: NameError: name 'my_set_data' is not defined, ya que la variable my_set_data ha sido eliminada

my_set_data2 = {"Brais", "Moure", 35}
print(my_set_data2)
my_list_data = list(my_set_data2) # Conversión de set a lista
print(type(my_list_data)) # Devuelve la lista convertida
my_set_data2.add("MoureDev") # Agrega un elemento al set
print(my_set_data2) # Devuelve el set con el nuevo elemento agregado

my_other_set_data = {"Kotlin", "Android", "Python", "Java"}

my_new_set_data = my_set_data2.union(my_other_set_data) # Unión de sets
print(my_new_set_data) # Devuelve el set con la unión de los dos sets

print(my_set_data2.intersection(my_other_set_data)) # Devuelve el set con los elementos en común de los dos sets
print(my_set_data2.difference(my_other_set_data)) # Devuelve el set con los elementos que están en el primer set pero no en el segundo
print(my_other_set_data.difference(my_set_data2)) # Devuelve el set con los elementos que están en el segundo set pero no en el primero
print(my_set_data2.symmetric_difference(my_other_set_data)) # Devuelve el set con los elementos que están en uno de los sets pero no en ambos

my_other_set_data.add("Android2") # Agrega un elemento al set
print(my_other_set_data) # Devuelve el set con el nuevo elemento agregado