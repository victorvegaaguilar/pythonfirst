#### Loops #####

my_condition = True

my_condition = False

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
for element in my_tuple:
    print(element)

my_set = {"Brais2", "Moure2", 351}

for element in my_set:
    print(element)

my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35}

for element in my_dict:
    print(element)
    if element == "Edad":
        print("Salio edad")
    else:
        print("No salio edad")




for element in list(my_dict.values()):
    print(element)


for element in my_dict:
    print(element)
    if element == "Edad":
        continue
        print("Salio edad")
else:
        print("El bucle para edad ha finalizado")
    