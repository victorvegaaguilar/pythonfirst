#### Higher Order Functions ####

from functools import reduce

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_one(number1, number2):
    return sum_one(number1 + number2)

print(sum_two_values_and_one(10,5))


def sum_two_values_and_one_with_function(number1, number2, f_sum):
    return f_sum(number1 + number2)

print(sum_two_values_and_one_with_function(10,5, sum_one))
print(sum_two_values_and_one_with_function(10,5, sum_five))


#### Closures ####

def sum_ten():
    def add(value):
        return value + 10
    return add

add_closure = sum_ten()
print(add_closure(5))


def sum_four(original_value):
    def add(value):
        return value + 4 + original_value
    return add

add_closure = sum_four(3)
print(add_closure(5))
print(sum_four(5)(3))

#### Closures ####

numbers = [2, 5, 10, 21, 30]

#Map

def multiply_two(number):
    return number * 2

print(list(map(multiply_two,numbers)))

# With lambda
print(list(map(lambda number: number * 2, numbers)))


# Filter

def filter_greater_than_ten(number):
    if number > 10:
        return True

    return False


print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce

def sum_two_values(number1, number2):
    return number1 + number2


print(reduce(sum_two_values,numbers))

