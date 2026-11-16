#### Lambdas ####

# sumar 2 numeros
sum_two_values = lambda number1, number2: number1 + number2
print(sum_two_values(3, 2))

multiply_values = lambda number1, number2: number1 * number2 - 3
print(multiply_values(3, 2))

def sum_three_values(value):
    return lambda number1, number2: number1 + number2 + value

print(sum_three_values(6)(7, 9))




