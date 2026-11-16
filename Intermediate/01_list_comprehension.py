#### List Comprehension ####

my_original_list = [35, 24, 62, 52, 30, 30, 17]
print(my_original_list)

my_list = [i for i in range(8)]
print(my_list)

my_list = [i + 1 for i in range(8)]
print(my_list)


my_list = [i * i for i in range(8)]
print(my_list)


def sum_five(numero1):
    return numero1 + 5



my_list = [sum_five(i) for i in range(8)]
print(my_list)