#### Error types ####

# SyntaxError
#print "Hola comunidad!" # Descomentar para error
print("Hola comunidad!")

# NameError
language = "Spanish" # Comentar para error
print(language)

# IndexError
my_list = ["aaaaa", "bbbbb", "ccccc"]
print(my_list[0])
#print(my_list[6]) # Descomentar para error

# ModuleError
#import maths # Descomentar para error
import math


# AttributeError
#print(math.PI) # Descomentar para error
print(math.pi)

# IndexError
my_dict = {"Nombre": "aaaaa", "Apellido": "bbbbb", "Alias": "ccccc"}
print(my_dict["Nombre"])
#print(my_dict["Nombre2"]) # Descomentar para error

# TypeError
my_list2 = ["aaaaa", "bbbbb", "ccccc"]
print(my_list2[0])
print(my_list2[True])
print(my_list2[False])
#print(my_list2["Nombre"]) # Descomentar para error

# ImportError
#from math import PI # Descomentar para error
from math import pi

# ValueError
#my_int = int("10 anios") # Descomentar para error
my_int = int("10")
print(type(my_int))

# ZeroDivisionError
#print(4/0) # Descomentar para error
print(4/2) 


