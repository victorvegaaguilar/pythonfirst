# Lists

my_list = [1, 2, 3, 4, 5]
print(my_list)
print(type(my_list)) # Devuelve el tipo de la variable

my_list2 = list() # Declaración de una lista vacía
print(my_list2)
my_list2.append(1) # Agrega un elemento al final de la lista
my_list2.append(2) # Agrega un elemento al final de la lista
print(my_list2)
print(len(my_list2)) # Devuelve la longitud de la lista


my_list3 = [] # Declaración de una lista vacía
print(my_list3)
my_list3 = [1, 2.0, "Hola"] # Declaración de una lista con elementos
print(my_list3)
print(type(my_list3)) # Devuelve el tipo de la variable

my_ages = [10, 20, 30, 40, 50, 30]
print(len(my_ages)) # Devuelve la longitud de la lista
print(my_ages[0]) # Devuelve el primer elemento de la lista
print(my_ages[-1]) # Devuelve el último elemento de la lista

print(my_ages[0:3]) # Devuelve los elementos desde el índice 0 hasta el índice 3 (sin incluir el índice 3)
print(my_ages[::2]) # Devuelve todos los elementos de la lista, pero solo los elementos en los índices pares
print(my_ages[::-1]) # Devuelve todos los elementos de la lista, pero en orden inverso  
print(my_ages[-5]) # Error: IndexError: list index out of range, ya que la lista tiene 5 elementos y el índice -5 no existe
print(my_ages.count(30)) # Devuelve el número de apariciones del elemento 30 en la list
my_ages.append(60) # Agrega un elemento al final de la lista
print(my_ages)
my_ages.insert(2, 25) # Agrega un elemento en el índice 2 de la lista
print(my_ages)
my_ages.remove(30) # Elimina la primera aparición del elemento 30 en la lista
print(my_ages)
my_ages.pop() # Elimina el último elemento de la lista
print(my_ages)
my_ages.sort() # Ordena la lista de menor a mayor
print(my_ages)
print(my_ages.index(40)) # Devuelve el índice del elemento 40 en la lista

print(my_ages.pop()) # Elimina el último elemento de la lista y lo devuelve
print(my_ages)

print(my_ages.reverse()) # Invierte el orden de la lista

my_new_ages = my_ages.copy() # Crea una copia de la lista


my_ages.clear() # Elimina todos los elementos de la lista
print(my_ages)

print(my_new_ages)

my_new_ages.sort()
print(my_new_ages)

print(my_new_ages[0:3]) # Devuelve los elementos desde el índice 0 hasta el índice 3 (sin incluir el índice 3)
print(my_new_ages[1:3]) # Devuelve los elementos desde el índice 1 hasta el índice 3 (sin incluir el índice 3)

print(my_new_ages)

del my_new_ages[0] # Elimina el elemento en el índice 0 de la lista
print(my_new_ages)

del my_new_ages # Elimina la variable my_new_ages
#print(my_new_ages) # Error: NameError: name 'my_new_ages' is not defined, ya que la variable my_new_ages ha sido eliminada



"""
data = [35, 1.70, "Juan", "Perez", True, 1 + 1j]
print(data)
age, height, name, surname, is_student, complex_number = data # Desempaquetado de listas
print(age)

# Concatenar listas
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2 # Concatenación de listas
print(list3)    

my_list = "Hola" # Declaración de una lista con un string
print(my_list) # Devuelve 'Hola'
print(type(my_list)) # Devuelve <class 'str'>, ya que la variable es un string y no una lista
"""




