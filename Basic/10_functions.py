#### Functions ####

def my_function():
    print("Esto es una funcion")


my_function()
my_function()

def sum_two_values(value1, value2):
    result = value1 + value2
    print(result)

sum_two_values(1, 2)

sum_two_values(23434, 3333)
sum_two_values("abc", "def")
sum_two_values(1.4, 5.3)

def substract_two_values(first_number:int, second_number:int):
    result = first_number - second_number
    print(result)

substract_two_values(23434, 33333)

#substract_two_values("abc", "def")


def sum_two_values_with_return(value1, value2):
    my_sum = value1 + value2
    return my_sum

my_result = sum_two_values_with_return(14, 53)

print(my_result)

def print_name(name = "Nombre1", surname = "Apellido1"):
    print(f"{name} {surname}")

print_name("Victor", "Vega")

def print_name_with_default(name, surname, alias = "Alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Victor", "Vega")

def print_texts(*texts):
    print(texts)

print_texts("aaaaa", "bbbb", "ccccc")

def print_texts_with_for(*texts):
    print(type(texts)) # type tuple
    for text in texts :
        print(text.upper())


print_texts_with_for("aaaaa", "bbbb", "ccccc")