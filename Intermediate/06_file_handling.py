#### File Handling ####

#### .txt file

import os

#txt_file = open("Intermediate/my_file.txt", "r+") # r+ Leer y escribir
txt_file = open("Intermediate/my_file.txt", "w+") # w+ Leer y escribir
txt_file.write("Mi nombre es Victor\nMi apellido es Vega\n35\nY mi lenguaje preferido es Python")
#print(txt_file.read())
#print(txt_file.read(10))

#print(txt_file.readline())
#print(txt_file.readline())

for line in txt_file.readlines():
    print(line)

txt_file.write("\nalgo nuevo en el archivo")

print(txt_file.readline())

txt_file.close()

with open("Intermediate/my_file.txt", "a") as my_other_file: # a Append 
    my_other_file.write("\nSwift")

#os.remove("Intermediate/my_file.txt")


#### json file

import json

json_file = open("Intermediate/my_file.json", "w+") # w+ Leer y escribir


json_text = {
    "nombre": "aaaa", 
    "apellido": "bbbbb", 
    "age": 35,
    "languages": ["Python", "Swift"]}

#json.dump(json_text, json_file, indent = 8) # Con identacion, espacios para ordenar
json.dump(json_text, json_file, indent=4)

json_file.close()

with open("Intermediate/my_file.json") as my_json_file: # a Append 
    for line in my_json_file.readlines():
        print(line)

json_dict = json.load(open("Intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))

print(json_dict["nombre"])


#### csv file
import csv


csv_file = open("Intermediate/my_csv.csv", "w+") # w+ Leer y escribir


#cvs_file.write("aaa1,bbb1,ccc1\naaa2,bbb2,ccc2\naaa3,bbb3,ccc3\naaa4,bbb4,ccc4")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "languaje"])
csv_writer.writerow(["Victor", "Vega", "Python"])
csv_writer.writerow(["Jorge", "Torres", "Alfa"])

csv_file.close()

with open("Intermediate/my_csv.csv") as my_csv_file: # a Append 
    for line in my_csv_file.readlines():
        print(line)

#### .xlsx file
# import xlrd # Debe instalarse el modulo




#### xml file
import xml

