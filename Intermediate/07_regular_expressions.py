#### Regular Expressions ####

import re

my_string = "Esta es la leccion numero 7: . Leccion, sigue: Expresiones regulares"
my_other_string = "Esta no es la leccion numero 6: Manejo de ficheros"


#### match

# match dice si encuentra, o no, un patron
print(re.match("Esta es la leccion", my_string))

match = re.match("Esta es la leccion", my_string)

print(match)
span = match.span()

print(span)

start, end = span

print(my_string[start:end])

match = re.match("Esta no es la leccion", my_other_string)
#if not(match == None): # Otra forma de comprobar el none
#if not(match) != None: # Otra forma de comprobar el none
if not(match) == None:
    print(match)
    start, end = span
    print(my_string[start:end])


#### search

search = re.search("leccion", my_string)
print(search)
start, end = search.span()
print(my_string[start:end])


#### findall

findall = re.findall("leccion", my_string, re.I)
print(findall)


#### split

split = re.split(":", my_string)
print(split)



#### sub

#print(re.sub("leccion", "LECCION",my_string))
print(re.sub("leccion|Leccion", "LECCION",my_string)) # Cambia tanto "leccion" como tambien "Leccion"


#### patterns

print(re.sub("[l|L]eccion", "LECCION", my_string))
print("a")

pattern = r"[l|L]"
print(re.findall(pattern, my_string))

pattern = r"[a-z]"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[L].*"
print(re.findall(pattern, my_string))

# email validation
pattern = r"[L].*"
print(re.findall(pattern, my_string))