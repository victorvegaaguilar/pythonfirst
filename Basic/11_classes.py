#### Classes ####

from re import fullmatch


class EmptyPerson:
    pass

print(EmptyPerson)
print(EmptyPerson())

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


my_person = Person("Victor", "Vega")

print(f"{my_person.name} {my_person.surname}")


class Person2:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"

    def walk(self):
        print(f"Esta caminando {self.full_name}")

my_person2 = Person2("Victor2", "Vega2")

print(my_person2.full_name)

my_person2.walk()




class Person3:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name= f"{name} {surname} {alias}"
        self.__name = name # Propiedad privada
        self.__surname = surname
        self.__alias = alias

    def walk(self):
        print(f"Esta caminando {self.full_name}")

    def get_name(self):
        return self.__name

my_person3 = Person3("Victor2", "Vega2", "Maverick")

print(my_person3.full_name)

my_person3.walk()

my_person3.full_name = "Hector de Leon, el chico de la calle"

print(my_person3.full_name)


my_person3.full_name = 7777

print(my_person3.full_name)

my_person3.get_name()


